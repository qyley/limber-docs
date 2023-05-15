gnrc_stream_cross_bar
------------------------------------------------
| Stream Cross Bar
| Connect ``N_IN`` AXI-stream-like input to ``N_OUT`` AXI-stream-like output
  routed by ``dest_i``.
| Use ``N_OUT`` `gnrc_stream_mux` and ``N_IN`` `gnrc_stream_demux`.


Parameters
````````````````````````````````````````````````


.. csv-table::
 :header: "parameter", "datatype", "range", "description"
 :widths: 2, 2, 2, 4
 
 "N_IN", "int", ">=1", "Number of Subordinate port (i.e. inputs port)."
 "N_OUT", "int", ">=1", "Number of Manager port (i.e. outputs port)."
 "DTYPE", "type", "logic", "data type of each port."
 "ARB_MODE", "bit [1:0]", "{0,1,2,3}", "Mode of arbitration. see `gnrc_arbiter` for detail. 

 0: Fix-priority (LSB has the most priority) 

 1: Unfair round-robin (i.e. depth=0) 

 2: Fair round-robin without look-ahead (i.e. depth=1) 

 3: Fair round-robin with look-ahead (i.e. depth=2)"
 "MAP", "logic[N_IN-1:0][N_OUT-1:0]", "N_IN*N_OUT matrix of bit {0,1}", "Bit Map of Connectivity. Use a N_IN * N_OUT bit map to set the connectivity between each input and output. set the bit of MAP(n,m) to '1' to connect the n-th input to m-th output. Full connect as default if this param hasn't been overrided."
 "OBUF", "bit", "{0,1}", "Adds a register slice at each output."
 "PRIVATE_ADDR", "bit", "{0,1}", "Set to 1 to use the private address of `dest_i` and `id_o` for each port. Set to 0 to use a global address of `dest_i` and `id_o` for each port."
 "DEST_T", "type", "logic [$clog2(N_OUT)-1:0]", "dest address bit width of each manager port (auto-gen, do **NOT** change)."
 "ID_T", "type", "logic [$clog2(N_IN)-1:0]", "source address bit width of each subordinate port (auto-gen, do **NOT** change)."
 


IOs
````````````````````````````````````````````````

.. csv-table::
 :header: "signal", "I/O", "width", "description"
 :widths: 2, 1, 2, 3
   
 "clk_i", "input", "logic", "Clock, positive edge triggered."
 "rst_ni", "input", "logic", "Asynchronous reset, active low."
 "flush_i", "input", "logic", "Clears the OBUF and arbiter."
 "data_i", "input", "DTYPE [N_IN-1:0]", "Subordinate ports for input data."
 "valid_i", "input", "logic [N_IN-1:0]", "Subordinate ports for valid flag of input data."
 "last_i", "input", "logic [N_IN-1:0]", "Subordinate ports for last flag of input data."
 "dest_i", "input", "DEST_T [N_IN-1:0]", "Subordinate ports for destination of input data."
 "ready_o", "output", "logic [N_IN-1:0]", "Subordinate port for ready flag of input data."
 "data_o", "output", "DTYPE [N_OUT-1:0]", "Manager ports for output data."
 "valid_o", "output", "logic [N_OUT-1:0]", "Manager ports for valid flag of output data."
 "last_o", "output", "logic [N_OUT-1:0]", "Manager ports for last flag of output data."
 "id_o", "output", "ID_T [N_OUT-1:0]", "Manager ports for source address of output data."
 "ready_i", "input", "logic [N_OUT-1:0]", "Manager ports for ready flag of output data."
 

Sketch
````````````````````````````````````````````````

.. image :: img/stream_cross_bar.svg


Private address vs. Global address
````````````````````````````````````````````````

Private address
  Private address 模式下每个端口只对自己可达的对方端口进行地址编码，忽略掉不可达的对方端口。

Global address
  Global address 模式下每个端口会对所有存在的对方端口（不考虑是否可达）进行地址编码。
  
例子：在 `Sketch`_ 展示的情况下， ``IN3`` 端口和 ``OUT3`` 端口的地址表如下表所示。

+------------+-----------+-----------+
| ``IN3``    |  destination port     |
+============+===========+===========+
| ``dest_i`` | Private   | Global    |
+------------+-----------+-----------+
|  2'b00     | ``OUT0``  | ``OUT0``  |
+------------+-----------+-----------+
|  2'b01     | ``OUT3``  | NC        |
+------------+-----------+-----------+
|  2'b10     | NC        | NC        |
+------------+-----------+-----------+
|  2'b11     | NC        | ``OUT3``  |
+------------+-----------+-----------+


+----------+-----------+-----------+
| ``OUT3`` |  source port          |
+==========+===========+===========+
| ``id_o`` | Private   | Global    |
+----------+-----------+-----------+
|  2'b00   | ``IN0``   | ``IN0``   |
+----------+-----------+-----------+
|  2'b01   | ``IN2``   |  NC       |
+----------+-----------+-----------+
|  2'b10   | ``IN3``   | ``IN2``   |
+----------+-----------+-----------+
|  2'b11   | NC        | ``IN3``   |
+----------+-----------+-----------+
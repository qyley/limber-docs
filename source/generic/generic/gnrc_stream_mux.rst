gnrc_stream_mux
------------------------------------------------
| Stream Multiplexer
| Arbitrate N AXI-stream-like input to single AXI-stream-like output.
| Arbitration will be switched after the last data of transaction.


Parameters
````````````````````````````````````````````````


.. csv-table::
 :header: "parameter", "datatype", "range", "description"
 :widths: 2, 2, 2, 4
 
 "N", "int", ">=1", "Number of inputs port."
 "DTYPE", "type", "logic", "data type of each port."
 "ARB_MODE", "bit [1:0]", "{0,1,2,3}", "Mode of arbitration. see `gnrc_arbiter` for detail. 

 0: Fix-priority (LSB has the most priority) 

 1: Unfair round-robin (i.e. depth=0) 

 2: Fair round-robin without look-ahead (i.e. depth=1) 

 3: Fair round-robin with look-ahead (i.e. depth=2)"
 "AW", "int", "$clog2(N)", "source address bit width of manager port (auto-gen, do **NOT** change)."
 


IOs
````````````````````````````````````````````````

.. csv-table::
 :header: "signal", "I/O", "width", "description"
 :widths: 2, 1, 2, 3
   
 "clk_i", "input", "logic", "Clock, positive edge triggered."
 "rst_ni", "input", "logic", "Asynchronous reset, active low."
 "flush_i", "input", "logic", "Clears the arbiter state. Only used if `ARB_MODE` is 0."
 "data_i", "input", "DTYPE [N-1:0]", "Subordinate ports for input data."
 "valid_i", "input", "logic [N-1:0]", "Subordinate ports for valid flag of input data."
 "last_i", "input", "logic [N-1:0]", "Subordinate ports for last flag of input data."
 "ready_o", "output", "logic [N-1:0]", "Subordinate ports for ready flag of input data."
 "data_o", "output", "DTYPE", "Manager port for output data."
 "valid_o", "output", "logic", "Manager port for valid flag of output data."
 "last_o", "output", "logic", "Manager port for last flag of output data."
 "id_o", "output", "logic [AW-1:0]", "Manager port for source address of output data."
 "ready_i", "input", "logic", "Manager port for ready flag of output data."
 

Sketch
````````````````````````````````````````````````

.. image :: img/stream_mux.svg
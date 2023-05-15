gnrc_stream_share_bus
------------------------------------------------
| Stream Share Bus
| Connect 1 of ``N_IN`` AXI-stream-like input to 1 of ``N_OUT`` AXI-stream-like output,
  routed by `dest_i`.
| use a `gnrc_stream_mux` and a `gnrc_stream_demux`.


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
 "OBUF", "bit", "{0,1}", "Adds a register slice at each output."
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

.. image :: img/stream_share_bus.svg
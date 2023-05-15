gnrc_stream_demux
------------------------------------------------
| Stream DeMultiplexer
| Switch single AXI-stream-like input to
  1 of N AXI-stream-like output by ``dest_i``.


Parameters
````````````````````````````````````````````````


.. csv-table::
 :header: "parameter", "datatype", "range", "description"
 :widths: 2, 2, 2, 4
 
 "N", "int", ">=1", "Number of inputs port."
 "DTYPE", "type", "logic", "data type of each port."
 "AW", "int", "$clog2(N)", "dest address bit width of each port (auto-gen, do **NOT** change)."
 


IOs
````````````````````````````````````````````````

.. csv-table::
 :header: "signal", "I/O", "width", "description"
 :widths: 2, 1, 2, 3
   
 "data_i", "input", "DTYPE", "Subordinate port for input data."
 "valid_i", "input", "logic", "Subordinate port for valid flag of input data."
 "dest_i", "input", "logic [AW-1:0]", "Subordinate port for destination of input data."
 "ready_o", "output", "logic", "Subordinate port for ready flag of input data."
 "data_o", "output", "DTYPE [N-1:0]", "Manager ports for output data."
 "valid_o", "output", "logic [N-1:0]", "Manager ports for valid flag of output data."
 "ready_i", "input", "logic [N-1:0]", "Manager ports for ready flag of output data."
 

Sketch
````````````````````````````````````````````````

.. image :: img/stream_demux.svg
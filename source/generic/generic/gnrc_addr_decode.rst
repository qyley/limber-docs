gnrc_addr_decode
------------------------------------------------
| addr decoder.
| There are 2 Format of Address Mapping Rule

1. Top of range (TOR)

  In ``TOR`` format, the address space will seperated into NR+1 intervals
  by NR Address Mapping Rule. The range of Eech intervals is as below:

    [0, MAP[0]-1], [MAP[1], MAP[2]-1] ..., [MAP[n], MAP[n+1]-1] ..., [MAP[NR], 2^AW-1]

  The value of ``MAP`` rules must be increasing across its 1st dimension

  For example, try:

.. code:: verilog

    // range of intervals are: [0,99], [100,199], [200,255]
    localparam logic[1:0][7:0] RULE_MAP_TOR = {
        8'd200,
        8'd100
    };

2. Naturally Aligned Power-Of-Two (NAPOT)

  In ``NAPOT`` format, the address space will be described as ``yyy...y011...1``
  where the ``yyy...y`` can be any number. The ``yyy...y011...1`` means
  the address space start from ``yyy...y000...0`` and end in ``yyy...y111...1`` .
  
  Requires the start address of ``MAP`` rules must be increasing across its
  1st dimension and with no overlap.

  For example, try:

.. code:: verilog

    // range of address space are: [0,127], [128,191]
    // and the out of range (i.e. non-allocated) space are: [192,255]
    localparam logic[1:0][7:0] RULE_MAP_NAPOT = {
        8'b1001_1111, // 1000_0000~1011_1111
        8'b0011_1111  // 0000_0000~0111_1111
    };


Parameters
````````````````````````````````````````````````


.. csv-table::
 :header: "parameter", "datatype", "range", "description"
 :widths: 2, 2, 2, 4
 
 "AW", "int unsigned", ">=1", "address bit width"
 "NR", "int unsigned", ">=1", "num of address mapping rule"
 "NAPOT", "bit", "{0,1}", "set 1 use `NAPOT` as the Format of Address Mapping Rule, set 0 use `TOR` as the Format of Address Mapping Rule"
 "MAP", "logic[NR-1:0][AW-1:0]", "!=0,-1", "address mapping rule data structure"
 


IOs
````````````````````````````````````````````````

.. csv-table::
 :header: "signal", "I/O", "width", "description"
 :widths: 2, 1, 2, 3
   
 "addr_i", "input", "logic[AW-1:0]", "address input"
 "map_idx_o", "output", "logic[CW-1:0]", "mapping range idx"
 "map_out_of_range_o", "output", "logic", "mapping out of range"
 


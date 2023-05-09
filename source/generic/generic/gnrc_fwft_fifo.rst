gnrc_fwft_fifo
------------------------------------------------
|
| Synchronous First-Word-Fall-Through FIFO
|
| This module need zero delay RAM(i.e read data can output instantly).
| Suitable for implementation of shallow depth FIFO in FPGA.
| If you need a deep depth FIFO, please see `gnrc_fifo` or `gnrc_mem2fifo`

Notation:
   
  A combinational path exists between output and input in this module.
  In the case of write a data when FIFO is empty,
  the input ``data_i`` will immediately output to ``data_o`` .
  This feature like a latch is useful under some situations.
  However if you wan to avoid this, use `gnrc_fifo` or `gnrc_mem2fifo`.


Parameters
````````````````````````````````````````````````


.. csv-table::
 :header: "parameter", "datatype", "range", "description"
 :widths: 2, 2, 2, 4
 
 "DW", "int(default)", ">=1", "Data bit width"
 "DP", "int(default)", ">=1", "FIFO depth"
 


IOs
````````````````````````````````````````````````

.. csv-table::
 :header: "signal", "I/O", "width", "description"
 :widths: 2, 1, 2, 3
   
 "clk_i", "input", "logic", "Clock, positive edge triggered."
 "rst_ni", "input", "logic", "Asynchronous reset, active low."
 "flush_i", "input", "logic", "Clears all data in FIFO."
 "data_i", "input", "logic [DW-1:0]", "data input"
 "wen_i", "input", "logic", "write enable (push)"
 "ren_i", "input", "logic", "read enable (pop)"
 "full_o", "output", "logic", "FIFO full"
 "empty_o", "output", "logic", "FIFO empty"
 "data_o", "output", "logic [DW-1:0]", "data output"
 

First Word Fall Through
````````````````````````````````````````````````

此 FIFO 利用 分布式RAM 读数据0延迟的特性来实现 First Word Fall Through。
由于分布式RAM容量小，因此不适合将深度设置得太大。

此外，FWFT 还有类似 Latch 的特性。
当 FIFO 为空时，向 FIFO 写入的 ``data_i`` 会立刻出现在 ``data_o`` 上， ``empty_o`` 也会立刻清0。
该特性导致输入和输出之间存在组合逻辑路径，如果对这种特性没有需求，请改用 `gnrc_fifo` 或 `gnrc_mem2fifo`。


:numref:`timing` 展示了此 FIFO FWFT 特性的读写时序

.. wavedrom::
    :name: timing
    :caption: FWFT特性的读写时序

    {
      signal: [
      {name: 'CLK',        wave: 'P..........', period:1},
      {name: 'data_i',     wave: 'x.=====x...',data:['d0','d1','d2','d3','d4']},
      {name: 'wen_i',      wave: '0.1....0...',},
      {name: 'ren_i',      wave: '0...1....0.',},
      {name: 'data_o',     wave: 'x.=..====x.',data:['d0','d1','d2','d3','d4']},
      {name: 'empty_o',    wave: '1.0......1.',}
      ],

      head: {},
      config: {hscale: 1},
      foot:{tock: 0}
    }


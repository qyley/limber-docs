gnrc_mem2fifo
------------------------------------------------
|
| Convert a memory interface to FIFO interface
|

Notation:
 This module Need a dual-port memory 
 (like a simple dual-port RAM) connecting from outside


Parameters
````````````````````````````````````````````````


.. csv-table::
 :header: "parameter", "datatype", "range", "description"
 :widths: 2, 2, 2, 4
 
 "DW", "int(default)", ">=1", "Data bit width"
 "DP", "int(default)", ">=2", "FIFO depth"
 "FWFT", "bit", "{0,1}", "1 to enable First Word Fall Through FIFO, 0 for Standard FIFO."
 "DELAY", "int(default)", ">=0", "latency of read of memory which equal to the depth of FWFT buffer, useless if `FWFT` is 0"
 "BYPASS", "bit", "{0,1}", "Bypass `data_i` to `data_o` when fifo is empty. **Only use in FWFT mode** . If `BYPASS` activated, a combinational path exists between output and input. In the case of simultaneously read and write when FIFO is empty, data_o can derived directly from data_in. This feature is useful under some situations. However if you needn't this, set `BYPASS` = 0."
 "AW", "int(default)", "$clog2(DP)", "Address bit width (auto-gen, do **NOT** change)"
 "CW", "int(default)", "$clog2(DP+1)", "data counter bit width (auto-gen, do **NOT** change)"
 


IOs
````````````````````````````````````````````````

.. csv-table::
 :header: "signal", "I/O", "width", "description"
 :widths: 2, 1, 2, 3
   
 "clk_i", "input", "logic", "Clock, positive edge triggered. Must synchronous with memory's clock"
 "rst_ni", "input", "logic", "Asynchronous reset, active low."
 "fifo_flush_i", "input", "logic", "Clears all data in FIFO. flush can only clear registered data, **NO** effect on combinational path."
 "fifo_data_i", "input", "logic [DW-1:0]", "data input"
 "fifo_wen_i", "input", "logic", "write enable (push)"
 "fifo_ren_i", "input", "logic", "read enable (pop)"
 "fifo_full_o", "output", "logic", "FIFO full"
 "fifo_empty_o", "output", "logic", "FIFO empty"
 "fifo_data_o", "output", "logic [DW-1:0]", "data output"
 "fifo_cnt_o", "output", "logic [CW-1:0]", "number of data in FIFO , it may be **NOT** accurate in `FWFT` mode, and the scale of inaccuracy depends on the `DELAY` of the memory"
 "mem_wen_o", "output", "bit", "memory write enable"
 "mem_waddr_o", "output", "[AW-1:0]", "memory write address"
 "mem_wdata_o", "output", "[DW-1:0]", "memory write data"
 "mem_ren_o", "output", "bit", "memory read enable"
 "mem_raddr_o", "output", "[AW-1:0]", "memory read address"
 "mem_rdata_i", "input", "[DW-1:0]", "memory read data"


Usage
````````````````````````````````````````````````

`gnrc_mem2fifo` 模块可以将一个存储器接口转化为 FIFO 接口使用，便于利用自定义的存储器制造一块 FIFO。
存储器需要具备两个独立的读、写通道。


.. figure:: img/mem2fifo_usage.svg


FIFO Mode
````````````````````````````````````````````````

 
`gnrc_mem2fifo` 支持 First Word Fall Through 模式 和 Bypass 模式。

Standard FIFO
  标准模式下，FIFO的读取请求 ``ren_i`` 使能后， 数据需要经过几个时钟周期的延迟才会从 ``data_o`` 输出，读取延迟等于所使用的存储器的读取延迟。

FWFT FIFO
  ``FWFT`` 模式下，FIFO会预先将最前端的数据准备在 ``data_o``，当 ``ren_i`` 使能后 ``data_o`` 会切换至下一个输出，``FWFT`` 模式下从FIFO种读取数据没有延迟。

Bypass FIFO
  ``BYPASS`` 模式只能在 ``FWFT`` 模式已启用的情况下开启，在 ``BYPASS`` 模式下，FIFO除了具有 ``FWFT`` 的无延迟读数的特点，当FIFO为空时，向 FIFO 写入的数据也会立刻出现在输出端口上，实现无延迟写入，在FIFO为空时可以实现同时读写的无延迟透传。

:numref:`mem2fifo_t1` 、 :numref:`mem2fifo_t2` 、:numref:`mem2fifo_t3` 展示了 3种配置下的 FIFO 的读写时序



.. wavedrom::
    :name: mem2fifo_t1
    :caption: Standard FIFO的读写时序(BYPASS=0,FWFT=0)

    {
      signal: [
      {name: 'CLK',        wave: 'P................', period:1},
      {name: 'data_i',     wave: 'x=====x...====x..',data:['d0','d1','d2','d3','d4','d5','d6','d7','d8']},
      {name: 'wen_i',      wave: '01....0...1...0..',},
      {name: 'ren_i',      wave: '0..1...010.1...0.',},
      {name: 'data_o',     wave: 'x...====.=..====.',data:['d0','d1','d2','d3','d4','d5','d6','d7','d8']},
      {name: 'empty_o',    wave: '1.0......1.0...1.',}
      ],

      head: {},
      config: {hscale: 1},
      foot:{tock: 0}
    }

.. wavedrom::
    :name: mem2fifo_t2
    :caption: FWFT FIFO的读写时序(BYPASS=0,FWFT=1)

    {
      signal: [
      {name: 'CLK',        wave: 'P................', period:1},
      {name: 'data_i',     wave: 'x=====x...====x..',data:['d0','d1','d2','d3','d4','d5','d6','d7','d8']},
      {name: 'wen_i',      wave: '01....0...1...0..',},
      {name: 'ren_i',      wave: '0..1...010.1...0.',},
      {name: 'data_o',     wave: 'x.=.====.x.====x.',data:['d0','d1','d2','d3','d4','d5','d6','d7','d8']},
      {name: 'empty_o',    wave: '1.0......1.0...1.',}
      ],

      head: {},
      config: {hscale: 1},
      foot:{tock: 0}
    }

.. wavedrom::
    :name: mem2fifo_t3
    :caption: Bypass FIFO的读写时序(BYPASS=1,FWFT=1)

    {
      signal: [
      {name: 'CLK',        wave: 'P................', period:1},
      {name: 'data_i',     wave: 'x=====x...====x..',data:['d0','d1','d2','d3','d4','d5','d6','d7','d8']},
      {name: 'wen_i',      wave: '01....0...1...0..',},
      {name: 'ren_i',      wave: '0..1...0101...0..',},
      {name: 'data_o',     wave: 'x=..====.x====x..',data:['d0','d1','d2','d3','d4','d5','d6','d7','d8']},
      {name: 'empty_o',    wave: '10.......10...1..',}
      ],

      head: {},
      config: {hscale: 1},
      foot:{tock: 0}
    }


Skid Buffer
````````````````````````````````````````````````

通过将 ``FWFT`` 参数设置为 1 来开启 First Word Fall Through 配置，开启后会在 `gnrc_mem2fifo` 内部额外生成一个 `skid_buffer` ，用于对 RAM 数据进行预取与缓存，使FIFO总是能很快地将最前端的数据准备在 ``data_o`` 端口上。 `skid_buffer` 通过例化 `gnrc_fwft_fifo` 实现。下图展示了实现的部分细节。

.. figure:: img/mem2fifo_fwft.svg


Data counter
````````````````````````````````````````````````

在 FWFT 模式下，由于 `skid buffer` 的存在，FIFO 内的 data counter 计数可能会不准，如果要进行准确计数请在外部自己写个计数器来记。


Bypass
````````````````````````````````````````````````

通过设置 ``BYPASS`` 可以开启 BYPASS 模式，在 BYPASS模式下， FIFO 有类似 Latch 的特性。
当 FIFO 为空时，向 FIFO 写入的 ``data_i`` 会立刻出现在 ``data_o`` 上， ``empty_o`` 也会立刻清0。
该特性导致输入和输出之间存在组合逻辑路径，请见 :numref:`fwft_fifo_t0` 。


Flush
````````````````````````````````````````````````

``flush_i`` 信号只对寄存器起作用，因此当 ``BYPASS`` 启用时，``flush_i`` 无法清除旁路上的组合逻辑的输出。请见 :numref:`fwft_fifo_t2` 。


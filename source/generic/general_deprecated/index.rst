General deprecated
================================================

general_deprecated是以往Limber项目中使用的通用模块，设计时参考了蜂鸟e203的通用库，为兼容早期的工程特地保留，不再更新，请勿修改


目录：


+ `limber_gnrl_arbiter`_
+ `limber_gnrl_crc32`_
+ `limber_gnrl_dff`_
+ `limber_gnrl_dffl`_
+ `limber_gnrl_dfflr`_
+ `limber_gnrl_dffr`_
+ `limber_gnrl_div`_
+ `limber_gnrl_ffchain`_
+ `limber_gnrl_fifo_asyn`_
+ `limber_gnrl_fifo_syn`_
+ `limber_gnrl_flop_sync`_
+ `limber_gnrl_latch`_
+ `limber_gnrl_ramdp`_
+ `limber_gnrl_ramdp_nr`_
+ `limber_gnrl_ramsp`_
+ `limber_gnrl_ramsp_nr`_
+ `limber_gnrl_ramtdp`_
+ `limber_gnrl_rand`_
+ `limber_gnrl_rising`_
+ `limber_gnrl_slice`_
+ `limber_gnrl_slot_timer`_
+ `limber_sim_ram`_




limber_gnrl_arbiter
------------------------------------------------

limber_gnrl_arbiter是一个仲裁器，支持优先级仲裁与轮询仲裁两种模式。

+ Parameters：

.. csv-table::
   :header: "parameter", "datatype", "range", "description"
   :widths: 15, 10, 10, 50

   "N", "integer", ">=2",  "仲裁请求的个数"
   "RR", "integer", "{0,1}",  "0为优先级仲裁，1为轮询仲裁"


+ IOs：



.. csv-table::
   :header: "signal", "I/O", "width", "description"
   :widths: 15, 10, 10, 50

   "i_clk", "Input", 1,  "时钟"
   "i_rst", "Input", 1, "异步高有效复位"
   "i_lhb_req_valid", "Input", N, "输入请求"
   "o_lhb_req_grant", "Output", N, "仲裁结果"

::

    o_lhb_req_grant输出可以在i_lhb_req_valid输入的同一个时钟内产生


limber_gnrl_crc32
------------------------------------------------

limber_gnrl_crc32可以用于计算以太网的CRC32校验位

::

    生成多项式： G(x)= x^32 + x^26 + x^23 + x^22 + x^16 + x^12 + x^11 + x^10 + x^8  + x^7  + x^5  + x^4  + x^2  + x^1  + 1

+ Parameters：

    无


+ IOs：



.. csv-table::
   :header: "signal", "I/O", "width", "description"
   :widths: 15, 10, 10, 50

   "i_clk", "Input", 1,  "时钟"
   "i_rstn", "Input", 1, "异步低有效复位"
   "i_data", "Input", 8, "输入数据"
   "i_data_vld", "Input", 1, "数据有效"
   "i_clr", "Input", 1, "同步高有效复位"
   "o_crc_data", "Output", 32, "计算结果（寄存器输出）"
   "o_crc_next", "Output", 32, "计算结果（组合输出）"

::

    o_crc_data会在有效数据输入的下一个时钟周期输出CRC32计算结果
    o_crc_next会在有效数据输入的当前时钟周期立即输出CRC32计算结果


limber_gnrl_dff
------------------------------------------------

Verilog module DFF with no Load-enable, no reset.


+ Parameters：

.. csv-table::
   :header: "parameter", "datatype", "range", "description"
   :widths: 15, 10, 10, 50

   "DW", "integer", >=1,  "数据位宽"


+ IOs：

.. csv-table::
   :header: "signal", "I/O", "width", "description"
   :widths: 15, 10, 10, 50

   "clk", "Input", 1,  "时钟"
   "dnxt", "Input", DW, "寄存器输入数据"
   "qout", "Output", DW, "寄存器输出数据"


limber_gnrl_dffl
------------------------------------------------

Verilog module DFF with Load-enable, no reset.


+ Parameters：

.. csv-table::
   :header: "parameter", "datatype", "range", "description"
   :widths: 15, 10, 10, 50

   "DW", "integer", >=1,  "数据位宽"


+ IOs：

.. csv-table::
   :header: "signal", "I/O", "width", "description"
   :widths: 15, 10, 10, 50

   "clk", "Input", 1,  "时钟"
   "lden", "Input", 1,  "高有效置位"
   "dnxt", "Input", DW, "寄存器输入数据"
   "qout", "Output", DW, "寄存器输出数据"


limber_gnrl_dfflr
------------------------------------------------

Verilog module DFF with Load-enable, asynchronous high-active reset.


+ Parameters：

.. csv-table::
   :header: "parameter", "datatype", "range", "description"
   :widths: 15, 10, 10, 50

   "DW", "integer", >=1,  "数据位宽"


+ IOs：

.. csv-table::
   :header: "signal", "I/O", "width", "description"
   :widths: 15, 10, 10, 50

   "clk", "Input", 1,  "时钟"
   "rst", "Input", 1,  "异步高有效复位"
   "lden", "Input", 1,  "高有效置位"
   "dnxt", "Input", DW, "寄存器输入数据"
   "qout", "Output", DW, "寄存器输出数据"

::

    复位后的寄存器输出为0

limber_gnrl_dffr
------------------------------------------------

Verilog module DFF with asynchronous high-active reset.


+ Parameters：

.. csv-table::
   :header: "parameter", "datatype", "range", "description"
   :widths: 15, 10, 10, 50

   "DW", "integer", >=1,  "数据位宽"


+ IOs：

.. csv-table::
   :header: "signal", "I/O", "width", "description"
   :widths: 15, 10, 10, 50

   "clk", "Input", 1,  "时钟"
   "rst", "Input", 1,  "异步高有效复位"
   "dnxt", "Input", DW, "寄存器输入数据"
   "qout", "Output", DW, "寄存器输出数据"

::

    复位后的寄存器输出为0

limber_gnrl_div
------------------------------------------------

使用恢复余数法（Remiander Restoring）实现的整数除法器.


+ Parameters：

.. csv-table::
   :header: "parameter", "datatype", "range", "description"
   :widths: 15, 10, 10, 50

   "DW1", "integer", >=1,  "被除数数据位宽"
   "DW2", "integer", >=1,  "除数数据位宽"



+ IOs：

.. csv-table::
   :header: "signal", "I/O", "width", "description"
   :widths: 15, 10, 10, 50

   "i_clk", "Input", 1,  "时钟"
   "i_rst", "Input", 1,  "异步高有效复位"
   "i_clr", "Input", 1,  "同步高有效复位"
   "i_dividend", "Input", DW1,  "输入除数"
   "i_divisor", "Input", DW2,  "输入被除数"
   "i_valid", "Input", 1,  "输入有效"
   "o_quo", "Output", DW1, "商输出"
   "o_rem", "Output", DW2, "余数输出"
   "o_valid", "Output", 1, "输出有效"

::

    - 电路的时延为DW1个时钟周期。
    - 只支持两个无符号数的除法。
    - 有符号数的除法需要先取绝对值再输入此除法器，最后根据输入除数与被除数的符号对结果进行符号位的恢复。
    - 此除法器内部没有对输入数据进行存储，计算时需要在o_valid信号拉高前保持i_divisor信号不变。
    - 除法器在i_valid=1后开始计算，计算过程中输入的i_valid=1不会被计算，直到o_valid=1产生。
    - 在o_valid=1时输入i_valid=1也能进行正常的计算。


limber_gnrl_ffchain
------------------------------------------------

DFF chain.


+ Parameters：

.. csv-table::
   :header: "parameter", "datatype", "range", "description"
   :widths: 15, 10, 10, 50

   "DW", "integer", >=1,  "数据位宽"
   "DP", "integer", >=1,  "深度（DFF串联个数）"


+ IOs：

.. csv-table::
   :header: "signal", "I/O", "width", "description"
   :widths: 15, 10, 10, 50

   "clk", "Input", 1,  "时钟"
   "rst_asyn", "Input", 1,  "异步高有效复位"
   "si", "Input", DW, "数据输入"
   "so", "Output", DW, "数据输出"

::

    si输入的数据会在DP个时钟周期后从so输出


limber_gnrl_fifo_asyn
------------------------------------------------

Verilog module async FIFO.


+ Parameters：

.. csv-table::
   :header: "parameter", "datatype", "range", "description"
   :widths: 15, 10, 10, 50

   "DW", "integer", >=1,  "数据位宽"
   "AW", "integer", >=1,  "地址位宽"

::

    FIFO深度为2^AW


+ IOs：

.. csv-table::
   :header: "signal", "I/O", "width", "description"
   :widths: 15, 10, 10, 50

   "wclk", "Input", 1,  "写时钟"
   "wrst", "Input", 1,  "异步高有效写复位"
   "din", "Input", DW,  "写数据输入"
   "wen", "Input", 1,  "写使能"
   "empty", "Output", 1,  "FIFO真空（写时钟域）"
   "afull", "Output", 1,  "FIFO假满（写时钟域）"
   "rclk", "Input", 1,  "读时钟"
   "rrst", "Input", 1,  "异步高有效读复位"
   "dout", "Output", DW,  "读数据输出"
   "ren", "Input", 1,  "读使能"
   "aempty", "Output", 1,  "FIFO假空（读时钟域）"
   "full", "Output", 1,  "FIFO真满（读时钟域）"

::

    - FIFO读写时钟域CDC使用深度为2的limber_gnrl_flop_sync同步
    - afull假满信号为高时wen将不起作用
    - aempty假空信号为高时ren将不起作用
    - 此FIFO为FWFT（First-word-Fall-Through）模式


limber_gnrl_fifo_syn
------------------------------------------------

Verilog module sync FIFO.

+ Parameters：

.. csv-table::
   :header: "parameter", "datatype", "range", "description"
   :widths: 15, 10, 10, 50

   "DW", "integer", >=1,  "数据位宽"
   "AW", "integer", >=1,  "地址位宽"
   "FORCE_X2ZERO", "integer", "{0,1}",  "1：仿真时强制令未初始化的数据为0，对电路综合没有影响"

::

    FIFO深度为2^AW


+ IOs：

.. csv-table::
   :header: "signal", "I/O", "width", "description"
   :widths: 15, 10, 10, 50

   "clk", "Input", 1,  "时钟"
   "rst", "Input", 1,  "异步高有效复位"
   "din", "Input", DW,  "写数据输入"
   "wen", "Input", 1,  "写使能"
   "ren", "Output", 1,  "读使能"
   "empty", "Output", 1,  "FIFO空"
   "full", "Input", 1,  "FIFO满"
   "dout", "Output", DW,  "读数据输出"

::

    - full为高时wen将不起作用
    - empty高时ren将不起作用
    - 此FIFO为FWFT（First-word-Fall-Through）模式


limber_gnrl_flop_sync
------------------------------------------------

Verilog module N-depth DFF Synchronizer.

+ Parameters：

.. csv-table::
   :header: "parameter", "datatype", "range", "description"
   :widths: 15, 10, 10, 50

   "DP", "integer", >=1,  "深度（FF级数）"
   "DW", "integer", >=1,  "数据位宽"


+ IOs：

.. csv-table::
   :header: "signal", "I/O", "width", "description"
   :widths: 15, 10, 10, 50

   "clk", "Input", 1,  "时钟B"
   "rst", "Input", 1,  "异步高有效复位"
   "din", "Input", DW,  "输入数据（时钟A）"
   "dout", "Input", DW,  "输出数据（时钟B）"

::

    对DW>=2的数据使用flop_sync同步需要使用格雷码


limber_gnrl_latch
------------------------------------------------

Verilog module Latch.

+ Parameters：

.. csv-table::
   :header: "parameter", "datatype", "range", "description"
   :widths: 15, 10, 10, 50

   "DW", "integer", >=1,  "数据位宽"


+ IOs：

.. csv-table::
   :header: "signal", "I/O", "width", "description"
   :widths: 15, 10, 10, 50

   "lden", "Input", 1,  "置数使能"
   "dnxt", "Input", DW,  "数据输入"
   "qout", "Input", DW,  "锁存数据输出"

::

    不推荐在FPGA中使用锁存器


limber_gnrl_ramdp
------------------------------------------------

Verilog module Dual port RAM.

+ Parameters：

.. csv-table::
   :header: "parameter", "datatype", "range", "description"
   :widths: 15, 10, 10, 50

   "DP", "integer", >=1,  "RAM深度"
   "DW", "integer", >=1,  "数据位宽"
   "AW", "integer", "=$clog2(DP)",  "地址位宽"
   "DLY", "integer", >=0,  "读操作时钟延迟"
   "FORCE_X2ZERO", "integer", "{0,1}",  "1：仿真时强制令未初始化的数据为0，对电路综合没有影响"


+ IOs：

.. csv-table::
   :header: "signal", "I/O", "width", "description"
   :widths: 15, 10, 10, 50

   "clk", "Input", 1,  "时钟"
   "din", "Input", DW,  "数据输入"
   "waddr", "Input", AW,  "写地址"
   "raddr", "Input", AW,  "读地址"
   "cs", "Input", 1,  "片选"
   "we", "Input", 1,  "写使能"
   "dout", "Input", DW,  "数据输出"

::

    该模块可以综合


limber_gnrl_ramdp_nr
------------------------------------------------

Verilog module Dual port RAM without output register.

+ Parameters：

.. csv-table::
   :header: "parameter", "datatype", "range", "description"
   :widths: 15, 10, 10, 50

   "DP", "integer", >=1,  "RAM深度"
   "DW", "integer", >=1,  "数据位宽"
   "AW", "integer", "=$clog2(DP)",  "地址位宽"
   "FORCE_X2ZERO", "integer", "{0,1}",  "1：仿真时强制令未初始化的数据为0，对电路综合没有影响"


+ IOs：

.. csv-table::
   :header: "signal", "I/O", "width", "description"
   :widths: 15, 10, 10, 50

   "clk", "Input", 1,  "时钟"
   "din", "Input", DW,  "数据输入"
   "waddr", "Input", AW,  "写地址"
   "raddr", "Input", AW,  "读地址"
   "cs", "Input", 1,  "片选"
   "we", "Input", 1,  "写使能"
   "dout", "Input", DW,  "数据输出"

::

    该模块是过时的，建议使用DLY=0的limber_gnrl_ramdp模块替代


limber_gnrl_ramsp
------------------------------------------------

Verilog module Single port RAM.

+ Parameters：

.. csv-table::
   :header: "parameter", "datatype", "range", "description"
   :widths: 15, 10, 10, 50

   "DP", "integer", >=1,  "RAM深度"
   "DW", "integer", >=1,  "数据位宽"
   "AW", "integer", "=$clog2(DP)",  "地址位宽"
   "DLY", "integer", >=0,  "读操作时钟延迟"
   "FORCE_X2ZERO", "integer", "{0,1}",  "1：仿真时强制令未初始化的数据为0，对电路综合没有影响"


+ IOs：

.. csv-table::
   :header: "signal", "I/O", "width", "description"
   :widths: 15, 10, 10, 50

   "clk", "Input", 1,  "时钟"
   "din", "Input", DW,  "数据输入"
   "addr", "Input", AW,  "读/写地址"
   "cs", "Input", 1,  "片选"
   "we", "Input", 1,  "读写切换（1：写，0：读）"
   "dout", "Input", DW,  "数据输出"

::

    该模块可以被综合


limber_gnrl_ramsp_nr
------------------------------------------------

Verilog module Single port RAM.

+ Parameters：

.. csv-table::
   :header: "parameter", "datatype", "range", "description"
   :widths: 15, 10, 10, 50

   "DP", "integer", >=1,  "RAM深度"
   "DW", "integer", >=1,  "数据位宽"
   "AW", "integer", "=$clog2(DP)",  "地址位宽"
   "FORCE_X2ZERO", "integer", "{0,1}",  "1：仿真时强制令未初始化的数据为0，对电路综合没有影响"


+ IOs：

.. csv-table::
   :header: "signal", "I/O", "width", "description"
   :widths: 15, 10, 10, 50

   "clk", "Input", 1,  "时钟"
   "din", "Input", DW,  "数据输入"
   "addr", "Input", AW,  "读/写地址"
   "cs", "Input", 1,  "片选"
   "we", "Input", 1,  "读写切换（1：写，0：读）"
   "dout", "Input", DW,  "数据输出"

::

    该模块是过时的，建议使用DLY=0的limber_gnrl_ramsp模块替代


limber_gnrl_ramtdp
------------------------------------------------

Verilog module Ture Dual port RAM.

+ Parameters：

.. csv-table::
   :header: "parameter", "datatype", "range", "description"
   :widths: 15, 10, 10, 50

   "DP", "integer", ">=1",  "RAM深度"
   "DW", "integer", >=1,  "数据位宽"
   "AW", "integer", "=$clog2(DP)",  "地址位宽"
   "DLY", "integer", >=0,  "读操作时钟延迟"
   "FORCE_X2ZERO", "integer", "{0,1}",  "1：仿真时强制令未初始化的数据为0，对电路综合没有影响"


+ IOs：

.. csv-table::
   :header: "signal", "I/O", "width", "description"
   :widths: 15, 10, 10, 50

   "clk", "Input", 1,  "时钟"
   "cs", "Input", 1,  "片选"
   "dina", "Input", DW,  "数据输入（端口A）"
   "addra", "Input", AW,  "读/写地址（端口A）"
   "wa", "Input", 1,  "读/写切换（1：写，0：读）（端口A）"
   "douta", "Input", DW,  "数据输出（端口A）"
   "dinb", "Input", DW,  "数据输入（端口B）"
   "addrb", "Input", AW,  "读/写地址（端口B）"
   "wb", "Input", 1,  "读/写切换（1：写，0：读）（端口B）"
   "doutb", "Input", DW,  "数据输出（端口B）"

::

    该模块无法在FPGA上综合（无法自动映射为真双口BRAM），仅用于仿真
    向端口A与端口B的相同地址同时写入数据时将造成冲突，只保留端口A写入的数据，端口B的写入数据会被丢失


limber_gnrl_rand
------------------------------------------------

Verilog module Random LFSR.

+ Parameters：

.. csv-table::
   :header: "parameter", "datatype", "range", "description"
   :widths: 15, 10, 10, 50

   "LFSR_LEN", "integer", "{8,16,24,32,40,48,56,64}",  "LFSR长度"
   "RAND_LEN", "integer", ">=1, <=LFSR_LEN",  "随机数位宽"
   "SEED_LEN", "integer", ">=1, <=LFSR_LEN",  "随机种子位宽"

::

  LFSR生成多项式.  Based on Application Note:
  http://www.xilinx.com/support/documentation/application_notes/xapp052.pdf

+ IOs：

.. csv-table::
   :header: "signal", "I/O", "width", "description"
   :widths: 15, 10, 10, 50

   "i_clk", "Input", 1,  "时钟"
   "i_csr_seed_wdata", "Input", SEED_LEN,  "随机种子输入"
   "i_csr_seed_wen", "Input", 1,  "随机种子写使能"
   "o_csr_seed_rdata", "Output", SEED_LEN,  "随机种子输出"
   "o_csr_rand_rdata", "Output", RAND_LEN,  "随机数输出"

::

    使用LFSR产生的伪随机数之间存在移位模式（Shifting Pattern）的相关性
    即输出随机数的高位与上一个时钟输出随机数的低位相同
    引入输出的非线性变换可以打破这种相关性，提升伪随机性
    o_csr_seed_rdata从LFSR的低位向上截取SEED_LEN长度输出
    o_csr_rand_rdata从LFSR的高位向下截取RAND_LEN长度输出
    更新随机种子时i_csr_seed_wdata的值将被写入LFSR低位的SEED_LEN个bit


limber_gnrl_rising
------------------------------------------------

Rising edge detect.

+ Parameters：

    无


+ IOs：

.. csv-table::
   :header: "signal", "I/O", "width", "description"
   :widths: 15, 10, 10, 50

   "i_clk", "Input", 1,  "时钟"
   "i_rst", "Input", 1,  "异步高有效复位"
   "i_a", "Input", 1,  "输入信号"
   "o_a_pulse", "Output", 1,  "上升边沿检测脉冲输出"



limber_gnrl_slice
------------------------------------------------

This module is an implementation of register slice. It can cut off the back-pressure ready-valid combinational path in pipeline with 0 clock data forward delay.

+ Parameters：

.. csv-table::
   :header: "parameter", "datatype", "range", "description"
   :widths: 15, 10, 10, 50

   "DW", "integer", ">=1",  "数据位宽"


+ IOs：

.. csv-table::
   :header: "signal", "I/O", "width", "description"
   :widths: 15, 10, 10, 50

   "clk", "Input", 1,  "时钟"
   "rst", "Input", 1,  "异步高有效复位"
   "s_valid", "Input", 1,  "输入数据VALID（本模块作为从机）"
   "s_ready", "Output", 1,  "输入数据READY（本模块作为从机）"
   "s_data", "Input", DW,  "输入数据（本模块作为从机）"
   "m_valid", "Output", 1,  "输出数据VALID（本模块作为主机）"
   "m_ready", "Input", 1,  "输出数据READY（本模块作为主机）"
   "m_data", "Output", DW,  "输出数据（本模块作为主机）"

::

    该模块相当于深度为1的FWFT模式的FIFO
    m_ready到s_ready的组合路径会被切断
    但s_valid到m_valid以及s_data到m_data的组合路径没有被切断
    该模块缺少充分验证，慎用

limber_gnrl_slot_timer
------------------------------------------------

This is a value-configurable timer. Function is as blow:
1. When i_set=1, i_value will be set as expired time.
2. When i_clear=1, the timing number will be clear to 0.
3. When i_start=1, timing number will increase at each clock posedge, when i_start=0, timing will be suspend.
4. When timing number reach the expired time, o_expired will set 1, and timing will stop. Set i_clear=1 to clear and relaunch the timing.

+ Parameters：

.. csv-table::
   :header: "parameter", "datatype", "range", "description"
   :widths: 15, 10, 10, 50

   "TW", "integer", ">=1",  "timing_value数据位宽"
   "SW", "integer", ">=1",  "slot_value数据位宽"
   "IV", "integer", ">=1",  "timing_value复位后的初始值"
   "TB", "integer", ">=1",  "计数器+1的时钟基数"


+ IOs：

.. csv-table::
   :header: "signal", "I/O", "width", "description"
   :widths: 15, 10, 10, 50

   "i_clk", "Input", 1,  "时钟"
   "i_rst", "Input", 1,  "异步高有效复位"
   "i_start", "Input", 1,  "计时使能（电平触发）"
   "i_clear", "Output", 1,  "同步计时复位（不会清除储存的timing_value和slot_value）"
   "i_timing_value", "Input", TW,  "timing_value数据输入"
   "i_slot_value", "Output", SW,  "slot_value数据输入"
   "i_set", "Input", 1,  "使能置数timing_value和slot_value"
   "o_expired", "Output", 1,  "计时超时标志输出"

::

    该计数器不直接输出counter的值，只在计时达到设置的timing_value和slot_value后产生expired标志
    使用i_clear=1可以清除expired标志并将counter复位（不会清除储存的timing_value和slot_value）
    此计时器可以设置每次计时包含多少个slot以及每个slot包含多少个timing
    参数TB可以设置每经过多少个时钟周期产生一个timing
    因此从0开始计时到产生expired的总时长=slot_value*timing_value*TB*clock_period


limber_sim_ram
------------------------------------------------

Verilog module Single port RAM. read/write delay is 1 clk.

+ Parameters：

.. csv-table::
   :header: "parameter", "datatype", "range", "description"
   :widths: 15, 10, 10, 50

   "DP", "integer", ">=1",  "RAM深度"
   "DW", "integer", ">=1",  "RAM数据位宽"
   "MW", "integer", "=DW/8",  "掩码位宽"
   "AW", "integer", "=$clog2(DP)",  "地址位宽"
   "FORCE_X2ZERO", "integer", "{0,1}",  "1：仿真时强制令未初始化的数据为0"
   "INIT_EN", "integer", "{0,1}",  "1:使用INIT_SRC作为RAM初值"
   "INIT_SRC", "string", "file path",  "二进制MEM文件地址"


+ IOs：

.. csv-table::
   :header: "signal", "I/O", "width", "description"
   :widths: 15, 10, 10, 50

   "clk", "Input", 1,  "时钟"
   "din", "Input", DW,  "数据输入"
   "addr", "Input", AW,  "读/写地址"
   "cs", "Input", 1,  "片选"
   "we", "Input", 1,  "读写切换（1：写，0：读）"
   "wem", "Output", MW,  "写掩码（每位掩码对应1个字节的数据）"
   "dout", "Input", DW,  "数据输出"

::

    该模块可以综合，但建议只用于仿真时作为输出测试激励的激励源
    通过INIT_SRC参数可以很方便地将二进制测试激励存储与该RAM中
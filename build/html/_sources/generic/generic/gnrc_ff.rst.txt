gnrc_ff.svh
================================================

包含了未修改的common_cells中的registers.svh所有寄存器宏定义。


并根据自己编写代码的习惯，补充了以gnrc\_*命名的一组寄存器宏定义，新的宏修改了原来的寄存器输入顺序与缩写。

下表列举了新的寄存器宏名称，以及每种寄存器宏所拥有的输入信号类型，宏的输入顺序与表中的顺序一致。

.. csv-table::
   :header: "macros", "clk", "rst", "load", "clr", "d", "q", "reset_value"
   :widths: 2, 1, 1, 1, 1, 1, 1, 1

   "gnrc_ff", "pos", "", "", "", "√", "√", ""
   "gnrc_ffr", "pos", "sync high", "", "", "√", "√", "√"
   "gnrc_ffrn", "pos", "sync low", "", "", "√", "√", "√"
   "gnrc_ffar", "pos", "async high", "", "", "√", "√", "√"
   "gnrc_ffarn", "pos", "async low", "", "", "√", "√", "√"
   "gnrc_ffl", "pos", "", "sync high", "", "√", "√", ""
   "gnrc_fflr", "pos", "sync high", "sync high", "", "√", "√", "√"
   "gnrc_fflrn", "pos", "sync low", "sync high", "", "√", "√", "√"
   "gnrc_fflar", "pos", "async high", "sync high", "", "√", "√", "√"
   "gnrc_fflarn", "pos", "async low", "sync high", "", "√", "√", "√"
   "gnrc_fflarc", "pos", "async high", "sync high", "sync high", "√", "√", "√"
   "gnrc_fflarnc", "pos", "async low", "sync high", "sync high", "√", "√", "√"
   "gnrc_latch", "", "", "async high", "", "√", "√", ""


示例：
    实现一个寄存器
    
    + 位宽为8
    + 异步低有效复位
    + 同步clr
    + 使能
    + 上升沿触发
    + 复位初值为255

::

    logic [7:0] d,q;
    //调用寄存器不用在末尾加分号
    `gnrc_fflarnc(clk, arstn, load, clr, d, q, 255)


以往使用parameter来例化寄存器时，经常因为疏忽大意忘记修改寄存器位宽，导致与数据位宽不匹配造成错误

使用宏函数生成寄存器的优势在于能减少代码长度，并且寄存器位宽会自动匹配d、q信号的位宽


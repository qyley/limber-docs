gnrc_slice
------------------------------------------------
| Register Slice
|
| Decouples two sides of a ready/valid handshake to allow back-to-back transfers
| without a combinational path between input and output, thus pipelining the path.
|
| There are 4 kind of type for register slice:

Pass Through
    Connect input to output directly. Not pipelining.
    Enable if ``FORWARD_Q=0`` and ``BACKWARD_Q=0``
Forward Registered
    `data_i` and `valid_i` will be registered to decouple the forward path.
    Enable if ``FORWARD_Q=1`` and ``BACKWARD_Q=0``
Backward Registered
    `ready_i` will be registered to decouple the backward path.
    Enable if ``FORWARD_Q=0`` and ``BACKWARD_Q=1``
Full Registered
    registered all input signal to decouple the path thoroughly between input and output.
    Enable if ``FORWARD_Q=1`` and ``BACKWARD_Q=1``

|


Parameters
````````````````````````````````````````````````


.. csv-table::
 :header: "parameter", "datatype", "range", "description"
 :widths: 2, 2, 2, 4
 
 "DW", "int unsigned", ">=1", "Data width of the payload in bits. Lose efficacy if `DTYPE` is overwritten."
 "FORWARD_Q", "bit", "{0,1}", "Set to 1 to enable Forward register."
 "BACKWARD_Q", "bit", "{0,1}", "Set to 1 to enable Backward register."
 "DTYPE", "type", "logic [DW-1:0]", "Data type of the payload, can be overwritten with custom type. Only use of `DW`."
 


IOs
````````````````````````````````````````````````

.. csv-table::
 :header: "signal", "I/O", "width", "description"
 :widths: 2, 1, 2, 3
   
 "clk_i", "input", "logic", "Clock, positive edge triggered."
 "rst_ni", "input", "logic", "Asynchronous reset, active low."
 "flush_i", "input", "logic", "Clears the registed data in slice. makes **NO** effect on combinational path"
 "valid_i", "input", "logic", "Input source is valid."
 "data_i", "input", "DTYPE", "Input source data."
 "ready_o", "output", "logic", "Input destination is ready."
 "valid_o", "output", "logic", "Output source is valid."
 "data_o", "output", "DTYPE", "Output source data."
 "ready_i", "input", "logic", "Output destination is ready."


Pass Through
````````````````````````````````````````````````

直连。等于没有用register slice。

Forward registered
````````````````````````````````````````````````

.. image :: img/slice_forward.png


Valid(from source)/channel payload 路径被插入了registers。

对于destination来讲，其得到的valid/payload必然来自RS中的registers，即若payload为full，则valid(to destination）有效。
对于source来讲，ready(to source)表明在下一个cycle，内部registers可以接受新的payload。在如下两种情况下为高：1.当前payload为空；2.当前payload为full，但同时destination的ready为高。

Backward registered
````````````````````````````````````````````````

.. image :: img/slice_backward.png
  

这种模式下，forward control path/payload没有刻意插入registers，而backward control path/payload（尤其指ready from destination这条路上），被插入了registers。
对于source来讲，其valid和payload直接的交易对象是RS内部的registers，ready(to source)有效的条件是内部payload为空。

对于destination来讲，其交易的对象可能是RS内部的payload，也可能直接来自于source。valid（to destination)表明当前是否有有效的payload给destination，这分为两种情况：1.RS内部payload为full；2.若payload为空，但此时valid(from source)有效。

Full registered
````````````````````````````````````````````````

.. image :: img/slice_full.png
  

Full Registered就是前两者的集合，即在forward path和backward path上都插入了registers, 切断了相关的path。在forward path上，使用了两套registers，类似ping-pong buffer的实现方式。
对于source来讲，其直接交易对象是ping-pong buffer，ready(to source)在ping-pong buffer至少其中一组为空时有效。
对于destination来讲，其直接交易对象也仅是ping-pong buffer，valid(to destination)在ping-pong buffer不为空时有效。


Summary
````````````````````````````````````````````````

Register slice的使用可以打断forward control/payload path或者backward control/payload path，在timing比较紧张的时候，选择适当的模式可以提高bus的频率。当然，register slice的引入会增大size，引入latency，因此也不建议随意使用。
gnrc_fractional_counter
------------------------------------------------
| Fractional counter
|
| This counter can generate a Fractional clock frequency division on `overflow_o` output
| Also can be a normal counter with configurable single/periodic triggle mode,
| up/down count mode, max count value and count increment.
|
| This counter add(or minus) an increment value each clock if en_i=1,
  When counter exceed its boundary(the max or 0 for up/down mode), it will
  minus(or add) a max count value to keep counter in the range of [0, max].
| 
| Usage:
| to generate a pulse every 3.2 clock,
  which means counter need accumulate 10/32 or 5/16 every clock.
  by setting max = 15 and inc = 5, this counter can generate 5 `overflow_o` pulse
  every 16 clocks, it's apporximately to a clock frequency division by 3.2
| 
| set max = -1 and inc = 1 make counter be a normal counter


Parameters
````````````````````````````````````````````````

.. csv-table::
   :header: "parameter", "datatype", "range", "description"
   :widths: 2, 2, 2, 4
   
   "N", "int unsigned", ">=1", "The width of the Denominator and Numerator part of a Fractions Expression."
   


IOs
````````````````````````````````````````````````

.. csv-table::
   :header: "signal", "I/O", "width", "description"
   :widths: 2, 1, 2, 3
   
   "clk_i", "input", "logic", "clock input"
   "rst_ni", "input", "logic", "asynchronous low-active reset input"
   "mode_i", "input", "logic", "mode select input. if mode=0, counter will stop once overflow is assert and hold on until a new clr or ld. if mode=1, counter work periodically and overflow will not be hold."
   "down_i", "input", "logic", "Count up(0) or down(1)"
   "ld_i", "input", "logic", "load counter configure data(max, inc)"
   "max_i", "input", "logic [N-1:0]", "the max of counter's numerator, equivalent to the denominator minus 1"
   "inc_i", "input", "logic [N-1:0]", "increment of the numerator"
   "en_i", "input", "logic", "counter runing iff the en_i=1"
   "clr_i", "input", "logic", "synchronous reset the `cnt_o` and `overflow_o`"
   "cnt_o", "output", "logic [N-1:0]", "the fraction numerator part of the counter"
   "overflow_o", "output", "logic", "overflow assert if counter exceed boundary"
   


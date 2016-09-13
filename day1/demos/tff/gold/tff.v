module main (input  S1, output  D1, input  CLKIN);
wire  inst0_Q;
wire  inst1_O;
SB_DFF inst0 (.C(CLKIN), .D(inst1_O), .Q(inst0_Q));
SB_LUT4 #(.LUT_INIT(16'h6666)) inst1 (.I0(S1), .I1(inst0_Q), .I2(1'b0), .I3(1'b0), .O(inst1_O));
assign D1 = inst0_Q;
endmodule


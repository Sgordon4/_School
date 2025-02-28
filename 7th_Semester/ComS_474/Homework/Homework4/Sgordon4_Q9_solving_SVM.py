(* Content-type: application/vnd.wolfram.mathematica *)

(*** Wolfram Notebook File ***)
(* http://www.wolfram.com/nb *)

(* CreatedBy='Mathematica 12.0' *)

(*CacheID: 234*)
(* Internal cache information:
NotebookFileLineBreakTest
NotebookFileLineBreakTest
NotebookDataPosition[       158,          7]
NotebookDataLength[     44537,       1165]
NotebookOptionsPosition[     41093,       1103]
NotebookOutlinePosition[     41633,       1123]
CellTagsIndexPosition[     41590,       1120]
WindowFrame->Normal*)

(* Beginning of Notebook Content *)
Notebook[{
Cell[TextData[{
 StyleBox["Solving an SVM by hand based on KKT conditions", "Title"],
 "\nby Forrest Sheng Bao at Iowa State University\nCopyleft 2020\n\nAlthough \
necessary but not sufficient, the KKT conditions are sufficient for \
optimality if the problem is to minimize a convex function which is the case \
for an SVM in primal form. Therefore, from KKT conditions alone, we can solve \
an SVM by hand. "
}], "Text",
 CellChangeTimes->{{3.809478116116029*^9, 3.8094781518624773`*^9}, {
  3.809480133696885*^9, 3.809480245093891*^9}, {3.809481281118278*^9, 
  3.809481294369741*^9}},ExpressionUUID->"adb71a89-d562-47df-8324-\
6a36495c6a5b"],

Cell[TextData[StyleBox["Warm-up: Solving a system of equations in \
Mathematica", "Section"]], "Text",
 CellChangeTimes->{{3.8094781665983963`*^9, 3.8094781873751297`*^9}, {
  3.809479031733479*^9, 3.809479044584676*^9}, {3.8095360190979633`*^9, 
  3.809536022404251*^9}},ExpressionUUID->"d4281001-2bb3-46e0-989d-\
06a0ef7d711b"],

Cell[CellGroupData[{

Cell[BoxData[
 RowBox[{"Solve", "[", 
  RowBox[{
   RowBox[{"{", 
    RowBox[{
     RowBox[{
      RowBox[{"a1", "+", "a2"}], "==", "2"}], ",", " ", 
     RowBox[{
      RowBox[{"a1", "-", "a2"}], "==", "10"}]}], "}"}], ",", " ", 
   RowBox[{"{", 
    RowBox[{"a1", ",", " ", "a2"}], "}"}]}], "]"}]], "Input",
 CellChangeTimes->{{3.809474544338231*^9, 3.809474547449151*^9}, {
  3.809474676280059*^9, 3.809474684300686*^9}, {3.80947474608584*^9, 
  3.809474786601427*^9}, {3.809474825918688*^9, 3.809474828022256*^9}},
 CellLabel->"In[20]:=",ExpressionUUID->"d7fd43c0-1e1a-43c6-a25a-82658c8ea76f"],

Cell[BoxData[
 RowBox[{"{", 
  RowBox[{"{", 
   RowBox[{
    RowBox[{"a1", "\[Rule]", "6"}], ",", 
    RowBox[{"a2", "\[Rule]", 
     RowBox[{"-", "4"}]}]}], "}"}], "}"}]], "Output",
 CellChangeTimes->{3.80947802693314*^9},
 CellLabel->"Out[20]=",ExpressionUUID->"cf5fa7c2-8c1d-442e-89dc-69691adf891f"]
}, Open  ]],

Cell[TextData[StyleBox["Example 1: Just two samples, one for each class.", \
"Section"]], "Text",
 CellChangeTimes->{{3.809479022447198*^9, 3.809479075914804*^9}, {
  3.809535991714774*^9, 
  3.809536012148477*^9}},ExpressionUUID->"ed97af3f-f5e1-4ac0-a1c1-\
69273c6a9ff6"],

Cell["\<\
The plot below indicates two two samples, (1,1) of class +1, and (0,0) of \
class -1. Denote the first one as sample 1 and the second as sample 2. A \
well-trained SVM would be the one depicted by the blue line. \
\>", "Text",
 CellChangeTimes->{
  3.8094790743953753`*^9, {3.809479110932456*^9, 3.809479111022203*^9}, {
   3.809479162938669*^9, 3.809479170748658*^9}, {3.809479483902193*^9, 
   3.80947948920956*^9}, {3.809480753255446*^9, 3.809480753991024*^9}, {
   3.809481022841651*^9, 
   3.809481061790267*^9}},ExpressionUUID->"0b7d98c4-9102-4544-ae34-\
f089afb92879"],

Cell[CellGroupData[{

Cell[BoxData[{
 RowBox[{
  RowBox[{"plt1", "=", " ", 
   RowBox[{"ListPlot", "[", 
    RowBox[{
     RowBox[{"{", 
      RowBox[{"{", 
       RowBox[{"0", ",", "0"}], "}"}], "}"}], ",", " ", 
     RowBox[{"PlotStyle", "\[Rule]", 
      RowBox[{"{", 
       RowBox[{
        RowBox[{"AbsolutePointSize", "[", "20", "]"}], ",", " ", "Red"}], 
       "}"}]}], ",", " ", 
     RowBox[{"AspectRatio", "\[Rule]", "1"}], ",", " ", 
     RowBox[{"PlotRange", "\[Rule]", 
      RowBox[{"{", 
       RowBox[{
        RowBox[{"{", 
         RowBox[{
          RowBox[{"-", "0.1"}], ",", " ", "1.1"}], "}"}], ",", " ", 
        RowBox[{"{", 
         RowBox[{
          RowBox[{"-", "0.1"}], ",", " ", "1.1"}], "}"}]}], "}"}]}]}], 
    "]"}]}], ";"}], "\[IndentingNewLine]", 
 RowBox[{
  RowBox[{"plt2", "=", " ", 
   RowBox[{"ListPlot", "[", 
    RowBox[{
     RowBox[{"{", 
      RowBox[{"{", 
       RowBox[{"1", ",", "1"}], "}"}], "}"}], ",", " ", 
     RowBox[{"PlotStyle", "\[Rule]", 
      RowBox[{"{", 
       RowBox[{
        RowBox[{"AbsolutePointSize", "[", "20", "]"}], ",", " ", "Blue"}], 
       "}"}]}], ",", " ", 
     RowBox[{"AspectRatio", "\[Rule]", "1"}], ",", " ", 
     RowBox[{"PlotRange", "\[Rule]", "All"}]}], "]"}]}], 
  ";"}], "\[IndentingNewLine]", 
 RowBox[{
  RowBox[{"plt3", " ", "=", 
   RowBox[{"ListLinePlot", "[", 
    RowBox[{
     RowBox[{"{", 
      RowBox[{
       RowBox[{"{", 
        RowBox[{"0", ",", "1"}], "}"}], ",", 
       RowBox[{"{", 
        RowBox[{"1", ",", "0"}], "}"}]}], "}"}], ",", " ", 
     RowBox[{"PlotRange", "\[Rule]", "All"}], ",", " ", 
     RowBox[{"PlotStyle", "\[Rule]", 
      RowBox[{"{", 
       RowBox[{
        RowBox[{"Thickness", "[", ".01", "]"}], ",", " ", "Black"}], 
       "}"}]}]}], "]"}]}], ";"}], "\[IndentingNewLine]", 
 RowBox[{"Show", "[", 
  RowBox[{"plt1", ",", " ", "plt2", ",", " ", "plt3"}], "]"}]}], "Input",
 CellChangeTimes->{{3.8094807621747627`*^9, 3.809480786478533*^9}, {
  3.809480867188622*^9, 3.809480931807001*^9}, {3.809480977602133*^9, 
  3.8094810154493504`*^9}, {3.809481099809272*^9, 3.809481104860752*^9}, {
  3.809538149813225*^9, 3.809538188430691*^9}},
 CellLabel->"In[96]:=",ExpressionUUID->"4a9548ae-df9a-437e-90f4-a3af5227764e"],

Cell[BoxData[
 GraphicsBox[{{{}, {
     {RGBColor[1, 0, 0], AbsolutePointSize[20], AbsoluteThickness[1.6], 
      PointBox[{{0., 0.}, {0., 0.}}]}, {
      {RGBColor[1, 0, 0], AbsolutePointSize[20], AbsoluteThickness[
       1.6]}, {}}, {
      {RGBColor[1, 0, 0], AbsolutePointSize[20], AbsoluteThickness[
       1.6]}, {}}}, {{}, {}}}, {{}, {
     {RGBColor[0, 0, 1], AbsolutePointSize[20], AbsoluteThickness[1.6], 
      PointBox[{{1., 1.}, {1., 1.}}]}, {
      {RGBColor[0, 0, 1], AbsolutePointSize[20], AbsoluteThickness[
       1.6]}, {}}, {
      {RGBColor[0, 0, 1], AbsolutePointSize[20], AbsoluteThickness[
       1.6]}, {}}}, {{}, {}}}, {{}, {{{}, {}, 
      {GrayLevel[0], PointSize[
        NCache[
         Rational[7, 360], 0.019444444444444445`]], Thickness[0.01], 
       LineBox[{{0., 1.}, {1., 0.}}]}}, 
     {GrayLevel[0], PointSize[
       NCache[
        Rational[7, 360], 0.019444444444444445`]], Thickness[0.01]}, {
      {GrayLevel[0], PointSize[
        NCache[
         Rational[7, 360], 0.019444444444444445`]], Thickness[0.01]}, {}}, {
      {GrayLevel[0], PointSize[
        NCache[
         Rational[7, 360], 0.019444444444444445`]], Thickness[
       0.01]}, {}}}, {{}, {}}}},
  AspectRatio->1,
  Axes->{True, True},
  AxesLabel->{None, None},
  AxesOrigin->{0, 0},
  DisplayFunction->Identity,
  Frame->{{False, False}, {False, False}},
  FrameLabel->{{None, None}, {None, None}},
  FrameTicks->{{Automatic, Automatic}, {Automatic, Automatic}},
  GridLines->{None, None},
  GridLinesStyle->Directive[
    GrayLevel[0.5, 0.4]],
  ImageSize->{224., Automatic},
  Method->{
   "OptimizePlotMarkers" -> True, 
    "CoordinatesToolOptions" -> {"DisplayFunction" -> ({
        (Identity[#]& )[
         Part[#, 1]], 
        (Identity[#]& )[
         Part[#, 2]]}& ), "CopiedValueFunction" -> ({
        (Identity[#]& )[
         Part[#, 1]], 
        (Identity[#]& )[
         Part[#, 2]]}& )}},
  PlotRange->{{-0.1, 1.1}, {-0.1, 1.1}},
  PlotRangeClipping->True,
  PlotRangePadding->{{0, 0}, {0, 0}},
  Ticks->{Automatic, Automatic}]], "Output",
 CellChangeTimes->{{3.8095381776504087`*^9, 3.8095381895111313`*^9}},
 CellLabel->"Out[99]=",ExpressionUUID->"27ad8ad9-8b11-4387-8920-fee108e2ea32"]
}, Open  ]],

Cell[CellGroupData[{

Cell[TextData[{
 "First, using the gradient on the bias term that  ",
 Cell[BoxData[
  FormBox[
   RowBox[{
    RowBox[{
     UnderoverscriptBox["\[Sum]", 
      RowBox[{"k", "=", "1"}], "K"], 
     RowBox[{
      SubscriptBox["\[Lambda]", "k"], "yk"}]}], "=", "0"}], TraditionalForm]],
  ExpressionUUID->"975bf15f-4c99-4490-a05a-61b1439aedf1"],
 ", we have ",
 Cell[BoxData[
  FormBox[
   RowBox[{
    RowBox[{
     RowBox[{"(", GridBox[{
        {
         SubscriptBox["\[Lambda]", "1"], 
         SubscriptBox["\[Lambda]", "2"]}
       }], ")"}], 
     RowBox[{"(", GridBox[{
        {
         RowBox[{"+", "1"}]},
        {
         RowBox[{"-", "1"}]}
       }], ")"}]}], "=", "0"}], TraditionalForm]],ExpressionUUID->
  "887cf06e-5a88-4020-a574-af81b0b74d80"]
}], "ItemNumbered",
 CellChangeTimes->{{3.809478256642342*^9, 3.8094782972326*^9}, {
   3.809478330670816*^9, 3.809478419592328*^9}, {3.809478487234991*^9, 
   3.809478554787055*^9}, {3.809478587662901*^9, 3.809478599721542*^9}, {
   3.8094786465312977`*^9, 3.80947869192199*^9}, {3.809478793900857*^9, 
   3.80947879499472*^9}, {3.809478905724934*^9, 3.80947898410632*^9}, 
   3.809479016572723*^9, {3.8094791143403177`*^9, 3.809479156885045*^9}, {
   3.809480403091566*^9, 3.8094804315311527`*^9}, {3.809480584482793*^9, 
   3.809480639906886*^9}},ExpressionUUID->"a8e278eb-4b39-4600-a068-\
a4cb8d19a28f"],

Cell[TextData[{
 "Then, write one equation for each sample in the complementary slackness \
equation (Equation D in slides):  ",
 Cell[BoxData[{
  FormBox[
   RowBox[{
    RowBox[{
     SubscriptBox["\[Lambda]", "1"], "[", 
     RowBox[{
      RowBox[{
       RowBox[{"+", "1"}], "\[CenterDot]", " ", 
       RowBox[{"(", 
        RowBox[{
         RowBox[{
          RowBox[{"(", GridBox[{
             {"w1", "w2"}
            }], ")"}], 
          RowBox[{"(", GridBox[{
             {"1"},
             {"1"}
            }], ")"}]}], "+", 
         SubscriptBox["w", "b"]}], ")"}]}], "-", "1"}], "]"}], "=", "0"}], 
   TraditionalForm], "\[IndentingNewLine]", 
  FormBox[
   RowBox[{
    RowBox[{
     SubscriptBox["\[Lambda]", "2"], "[", 
     RowBox[{
      RowBox[{
       RowBox[{"-", "1"}], "\[CenterDot]", 
       RowBox[{"(", 
        RowBox[{
         RowBox[{
          RowBox[{"(", GridBox[{
             {"w1", "w2"}
            }], ")"}], 
          RowBox[{"(", GridBox[{
             {"0"},
             {"0"}
            }], ")"}]}], "+", 
         SubscriptBox["w", "b"]}], ")"}]}], "-", "1"}], "]"}], "=", "0"}], 
   TraditionalForm]}],ExpressionUUID->"972bcd1f-a0ae-47c4-9cc8-af09e4e1641f"]
}], "ItemNumbered",
 CellChangeTimes->{{3.809478256642342*^9, 3.8094782972326*^9}, {
   3.809478330670816*^9, 3.809478419592328*^9}, {3.809478487234991*^9, 
   3.809478554787055*^9}, {3.809478587662901*^9, 3.809478599721542*^9}, {
   3.8094786465312977`*^9, 3.80947869192199*^9}, {3.809478793900857*^9, 
   3.80947879499472*^9}, {3.809478905724934*^9, 3.80947898410632*^9}, 
   3.809479016572723*^9, {3.8094791143403177`*^9, 3.80947911489261*^9}, {
   3.8094792407403517`*^9, 3.809479262448217*^9}, {3.809479292516492*^9, 
   3.809479306780452*^9}, {3.809479372173217*^9, 3.809479398509343*^9}, {
   3.809479435464151*^9, 3.809479527543763*^9}, {3.8094795644737186`*^9, 
   3.809479604194919*^9}, {3.809480267839184*^9, 3.809480325616352*^9}, {
   3.8094805436040287`*^9, 3.809480578243908*^9}, {3.809480649053053*^9, 
   3.809480649053165*^9}, {3.8094812362710867`*^9, 
   3.809481237825612*^9}},ExpressionUUID->"6c2db023-8746-4aea-bc62-\
84b9e8189e8e"],

Cell[TextData[{
 "Finally, the gradient on the non-bias weights:  ",
 Cell[BoxData[
  FormBox[
   RowBox[{
    RowBox[{"(", GridBox[{
       {"w1"},
       {"w2"}
      }], ")"}], "=", 
    RowBox[{
     RowBox[{
      SubscriptBox["\[Lambda]", "1"], "\[CenterDot]", 
      RowBox[{"(", GridBox[{
         {"1"},
         {"1"}
        }], ")"}]}], "-", 
     RowBox[{
      SubscriptBox["\[Lambda]", "2"], "\[CenterDot]", 
      RowBox[{"(", GridBox[{
         {"0"},
         {"0"}
        }], ")"}]}]}]}], TraditionalForm]],ExpressionUUID->
  "72deb466-8e4f-47b0-a628-4b0540315cd1"]
}], "ItemNumbered",
 CellChangeTimes->{{3.809478256642342*^9, 3.8094782972326*^9}, {
   3.809478330670816*^9, 3.809478419592328*^9}, {3.809478487234991*^9, 
   3.809478554787055*^9}, {3.809478587662901*^9, 3.809478599721542*^9}, {
   3.8094786465312977`*^9, 3.80947869192199*^9}, {3.809478793900857*^9, 
   3.80947879499472*^9}, {3.809478905724934*^9, 3.80947898410632*^9}, 
   3.809479016572723*^9, {3.8094791143403177`*^9, 3.80947911489261*^9}, {
   3.8094792407403517`*^9, 3.809479262448217*^9}, {3.809479292516492*^9, 
   3.809479306780452*^9}, {3.809479372173217*^9, 3.809479398509343*^9}, {
   3.809479435464151*^9, 3.809479527543763*^9}, {3.8094795644737186`*^9, 
   3.8094797249991837`*^9}, {3.8094803313261137`*^9, 3.809480366800935*^9}, {
   3.809480440924625*^9, 3.809480444326388*^9}, {3.8094805949397182`*^9, 
   3.809480607758918*^9}},ExpressionUUID->"50f522f3-48fa-44d1-a642-\
a420f034480f"]
}, Open  ]],

Cell[TextData[{
 "Expand matrix operations above into a system of equations and solve them \
using the ",
 StyleBox["Solve", "CodeText"],
 " function. For typesetting easiness,  \[Lambda]\[CloseCurlyQuote]s are \
replaced with a\[CloseCurlyQuote]s in the code below."
}], "Text",
 CellChangeTimes->{{3.809478256642342*^9, 3.8094782972326*^9}, {
   3.809478330670816*^9, 3.809478419592328*^9}, {3.809478487234991*^9, 
   3.809478554787055*^9}, {3.809478587662901*^9, 3.809478599721542*^9}, {
   3.8094786465312977`*^9, 3.80947869192199*^9}, {3.809478793900857*^9, 
   3.80947879499472*^9}, {3.809478905724934*^9, 3.80947898410632*^9}, 
   3.809479016572723*^9, {3.8094791143403177`*^9, 3.80947911489261*^9}, {
   3.8094792407403517`*^9, 3.809479262448217*^9}, {3.809479292516492*^9, 
   3.809479306780452*^9}, {3.809479372173217*^9, 3.809479398509343*^9}, {
   3.809479435464151*^9, 3.809479527543763*^9}, {3.8094795644737186`*^9, 
   3.809479796320891*^9}, {3.809479896603436*^9, 3.809479926747126*^9}, {
   3.809480375641519*^9, 3.8094803771191463`*^9}, {3.8095383036900377`*^9, 
   3.809538315273353*^9}},ExpressionUUID->"0eb6bd6d-04ce-4aa1-b89c-\
7cb4d277c287"],

Cell[CellGroupData[{

Cell[BoxData[
 RowBox[{"Solve", "[", 
  RowBox[{
   RowBox[{"{", " ", 
    RowBox[{
     RowBox[{
      RowBox[{"a1", "-", "a2"}], "\[Equal]", " ", "0"}], ",", 
     "\[IndentingNewLine]", "         ", 
     RowBox[{
      RowBox[{"a1", " ", "*", 
       RowBox[{"(", 
        RowBox[{"w1", "+", "w2", " ", "+", "wb", "-", "1"}], ")"}]}], " ", 
      "\[Equal]", " ", "0"}], ",", "\[IndentingNewLine]", "         ", 
     RowBox[{
      RowBox[{"a2", " ", "*", 
       RowBox[{"(", 
        RowBox[{
         RowBox[{
          RowBox[{"-", "1"}], "*", "wb"}], "-", "1"}], ")"}]}], " ", 
      "\[Equal]", " ", "0"}], ",", "\[IndentingNewLine]", "         ", 
     RowBox[{"w1", " ", "\[Equal]", "  ", "a1"}], ",", "\[IndentingNewLine]", 
     "         ", 
     RowBox[{"w2", "\[Equal]", " ", "a1"}], ",", "\[IndentingNewLine]", 
     "         ", 
     RowBox[{
      RowBox[{"a1", " ", "+", " ", "a2"}], " ", "\[NotEqual]", " ", "0"}]}], 
    "\[IndentingNewLine]", "}"}], ",", " ", 
   RowBox[{"{", 
    RowBox[{"a1", ",", "a2", ",", "w1", ",", "w2", ",", "wb"}], "}"}]}], 
  "\[IndentingNewLine]", "]"}]], "Input",
 CellChangeTimes->{{3.809478231270335*^9, 3.809478242198053*^9}, {
  3.809479817710506*^9, 3.809479821396729*^9}, {3.8111222438800163`*^9, 
  3.811122264159978*^9}, {3.8111223070880313`*^9, 3.811122328287193*^9}},
 CellLabel->"In[1]:=",ExpressionUUID->"f8b97ad5-0070-42a2-b0ba-49f0338d964d"],

Cell[BoxData[
 RowBox[{"{", 
  RowBox[{"{", 
   RowBox[{
    RowBox[{"a1", "\[Rule]", "1"}], ",", 
    RowBox[{"a2", "\[Rule]", "1"}], ",", 
    RowBox[{"w1", "\[Rule]", "1"}], ",", 
    RowBox[{"w2", "\[Rule]", "1"}], ",", 
    RowBox[{"wb", "\[Rule]", 
     RowBox[{"-", "1"}]}]}], "}"}], "}"}]], "Output",
 CellChangeTimes->{3.809478243811109*^9, 3.809479824870523*^9, 
  3.8111223468992233`*^9},
 CellLabel->"Out[1]=",ExpressionUUID->"c3281e8d-8089-4eac-ae97-f586c71e18ef"]
}, Open  ]],

Cell[TextData[{
 "The first 3 solutions set both a1 and a2 to 0. They should be discarded as \
they remove the constraints from the Lagrange multiplier. \nThe last solution \
is what we want, demonstrating an equation ",
 Cell[BoxData[
  FormBox[
   RowBox[{
    RowBox[{"x", "+", "y", "-", "1"}], "=", "0"}], TraditionalForm]],
  ExpressionUUID->"4f91c532-fcd9-4f15-96c4-c32de221233c"],
 " which beautifully goes between the two samples at 135 degree. The fact \
that neither a1 nor a2 are zero indicates that both samples are the \
supporting vectors. "
}], "Text",
 CellChangeTimes->{{3.809479857082703*^9, 3.809479893180339*^9}, {
  3.809479938579204*^9, 3.809480043937777*^9}, {3.8094814142074413`*^9, 
  3.809481432887645*^9}, {3.809538495268077*^9, 
  3.809538497306623*^9}},ExpressionUUID->"54e97f20-029c-4bd4-b07b-\
b28ee1a48dde"],

Cell[TextData[StyleBox["Example 2", "Section"]], "Text",
 CellChangeTimes->{{3.809481265873765*^9, 3.809481268490934*^9}, {
  3.8095360403342943`*^9, 
  3.8095360477124147`*^9}},ExpressionUUID->"ee48dd51-a74f-4984-a51e-\
dc0bd061d2a6"],

Cell["\<\
Class +1: (0,0) and (0,1)
Class -1:  (1,0) and (1,1). \
\>", "Text",
 CellChangeTimes->{{3.809536049648138*^9, 3.809536118946156*^9}, {
  3.8095364810038967`*^9, 
  3.809536492867907*^9}},ExpressionUUID->"e01352ec-9ae0-4d87-986a-\
cdb9f4123047"],

Cell[CellGroupData[{

Cell[BoxData[{
 RowBox[{
  RowBox[{"plt1", "=", " ", 
   RowBox[{"ListPlot", "[", 
    RowBox[{
     RowBox[{"{", 
      RowBox[{
       RowBox[{"{", 
        RowBox[{"0", ",", "0"}], "}"}], ",", 
       RowBox[{"{", 
        RowBox[{"0", ",", " ", "1"}], "}"}]}], "}"}], ",", " ", 
     RowBox[{"PlotStyle", "\[Rule]", 
      RowBox[{"{", 
       RowBox[{
        RowBox[{"AbsolutePointSize", "[", "20", "]"}], ",", " ", "Red"}], 
       "}"}]}], ",", " ", 
     RowBox[{"AspectRatio", "\[Rule]", "1"}], ",", " ", 
     RowBox[{"PlotRange", "\[Rule]", 
      RowBox[{"{", 
       RowBox[{
        RowBox[{"{", 
         RowBox[{
          RowBox[{"-", "0.1"}], ",", " ", "1.1"}], "}"}], ",", " ", 
        RowBox[{"{", 
         RowBox[{
          RowBox[{"-", "0.1"}], ",", " ", "1.1"}], "}"}]}], "}"}]}]}], 
    "]"}]}], ";"}], "\[IndentingNewLine]", 
 RowBox[{
  RowBox[{"plt2", "=", " ", 
   RowBox[{"ListPlot", "[", 
    RowBox[{
     RowBox[{"{", 
      RowBox[{
       RowBox[{"{", 
        RowBox[{"1", ",", " ", "0"}], "}"}], ",", 
       RowBox[{"{", 
        RowBox[{"1", ",", "1"}], "}"}]}], "}"}], ",", " ", 
     RowBox[{"PlotStyle", "\[Rule]", 
      RowBox[{"{", 
       RowBox[{
        RowBox[{"AbsolutePointSize", "[", "20", "]"}], ",", " ", "Blue"}], 
       "}"}]}], ",", " ", 
     RowBox[{"AspectRatio", "\[Rule]", "1"}], ",", " ", 
     RowBox[{"PlotRange", "\[Rule]", "All"}]}], "]"}]}], 
  ";"}], "\[IndentingNewLine]", 
 RowBox[{
  RowBox[{"plt3", " ", "=", 
   RowBox[{"ListLinePlot", "[", 
    RowBox[{
     RowBox[{"{", 
      RowBox[{
       RowBox[{"{", 
        RowBox[{"0.5", ",", "0"}], "}"}], ",", 
       RowBox[{"{", 
        RowBox[{"0.5", ",", "1"}], "}"}]}], "}"}], ",", " ", 
     RowBox[{"PlotRange", "\[Rule]", "All"}], ",", " ", 
     RowBox[{"PlotStyle", "\[Rule]", 
      RowBox[{"{", 
       RowBox[{
        RowBox[{"Thickness", "[", ".01", "]"}], ",", " ", "Black"}], 
       "}"}]}]}], "]"}]}], ";"}], "\[IndentingNewLine]", 
 RowBox[{"Show", "[", 
  RowBox[{"plt1", ",", " ", "plt2", ",", " ", "plt3"}], "]"}]}], "Input",
 CellChangeTimes->{{3.809535942485824*^9, 3.8095359778971786`*^9}, {
  3.809536128098506*^9, 3.8095361607666197`*^9}, {3.809537615954858*^9, 
  3.8095376277551317`*^9}, {3.809537852134709*^9, 3.809537899984397*^9}},
 CellLabel->"In[88]:=",ExpressionUUID->"7871d66f-be0f-4091-a4e1-b2aac063d8e9"],

Cell[BoxData[
 GraphicsBox[{{{}, {
     {RGBColor[1, 0, 0], AbsolutePointSize[20], AbsoluteThickness[1.6], 
      PointBox[{{0., 0.}, {0., 1.}}]}, {
      {RGBColor[1, 0, 0], AbsolutePointSize[20], AbsoluteThickness[
       1.6]}, {}}, {
      {RGBColor[1, 0, 0], AbsolutePointSize[20], AbsoluteThickness[
       1.6]}, {}}}, {{}, {}}}, {{}, {
     {RGBColor[0, 0, 1], AbsolutePointSize[20], AbsoluteThickness[1.6], 
      PointBox[{{1., 0.}, {1., 1.}}]}, {
      {RGBColor[0, 0, 1], AbsolutePointSize[20], AbsoluteThickness[
       1.6]}, {}}, {
      {RGBColor[0, 0, 1], AbsolutePointSize[20], AbsoluteThickness[
       1.6]}, {}}}, {{}, {}}}, {{}, {{{}, {}, 
      {GrayLevel[0], PointSize[
        NCache[
         Rational[7, 360], 0.019444444444444445`]], Thickness[0.01], 
       LineBox[{{0.5, 0.}, {0.5, 1.}}]}}, 
     {GrayLevel[0], PointSize[
       NCache[
        Rational[7, 360], 0.019444444444444445`]], Thickness[0.01]}, {
      {GrayLevel[0], PointSize[
        NCache[
         Rational[7, 360], 0.019444444444444445`]], Thickness[0.01]}, {}}, {
      {GrayLevel[0], PointSize[
        NCache[
         Rational[7, 360], 0.019444444444444445`]], Thickness[
       0.01]}, {}}}, {{}, {}}}},
  AspectRatio->1,
  Axes->{True, True},
  AxesLabel->{None, None},
  AxesOrigin->{0, 0},
  DisplayFunction->Identity,
  Frame->{{False, False}, {False, False}},
  FrameLabel->{{None, None}, {None, None}},
  FrameTicks->{{Automatic, Automatic}, {Automatic, Automatic}},
  GridLines->{None, None},
  GridLinesStyle->Directive[
    GrayLevel[0.5, 0.4]],
  ImageSize->{237., Automatic},
  Method->{
   "OptimizePlotMarkers" -> True, 
    "CoordinatesToolOptions" -> {"DisplayFunction" -> ({
        (Identity[#]& )[
         Part[#, 1]], 
        (Identity[#]& )[
         Part[#, 2]]}& ), "CopiedValueFunction" -> ({
        (Identity[#]& )[
         Part[#, 1]], 
        (Identity[#]& )[
         Part[#, 2]]}& )}},
  PlotRange->{{-0.1, 1.1}, {-0.1, 1.1}},
  PlotRangeClipping->True,
  PlotRangePadding->{{0, 0}, {0, 0}},
  Ticks->{Automatic, Automatic}]], "Output",
 CellChangeTimes->{3.809536161848076*^9, 3.8095376386176643`*^9, 
  3.809537866296598*^9, 3.809537900930048*^9},
 CellLabel->"Out[91]=",ExpressionUUID->"1c977473-74dd-4c42-be8d-7408b809eb53"]
}, Open  ]],

Cell[CellGroupData[{

Cell[BoxData[
 RowBox[{"Solve", "[", 
  RowBox[{
   RowBox[{"{", 
    RowBox[{
     RowBox[{
      RowBox[{"a1", "+", "a2", "-", "a3", " ", "-", "a4"}], " ", "\[Equal]", 
      " ", "0"}], ",", "\[IndentingNewLine]", "         ", 
     RowBox[{
      RowBox[{"a1", " ", "*", 
       RowBox[{"(", 
        RowBox[{
         RowBox[{"1", "*", 
          RowBox[{"(", 
           RowBox[{"w1", "+", "w2", "+", "wb"}], ")"}]}], "-", "1"}], ")"}]}],
       "\[Equal]", "0"}], ",", "\[IndentingNewLine]", "         ", 
     RowBox[{
      RowBox[{"a2", "*", 
       RowBox[{"(", 
        RowBox[{
         RowBox[{"1", "*", 
          RowBox[{"(", 
           RowBox[{"w1", "+", " ", "0", "+", "  ", "wb"}], ")"}]}], "-", 
         "1"}], ")"}]}], "\[Equal]", "0"}], ",", "\[IndentingNewLine]", 
     "         ", 
     RowBox[{
      RowBox[{"a3", "*", 
       RowBox[{"(", 
        RowBox[{
         RowBox[{
          RowBox[{"-", "1"}], "*", 
          RowBox[{"(", 
           RowBox[{"0", "  ", "+", " ", "0", "+", "  ", "wb"}], ")"}]}], "-", 
         "1"}], ")"}]}], "\[Equal]", "0"}], ",", "\[IndentingNewLine]", 
     "         ", 
     RowBox[{
      RowBox[{"a4", "*", 
       RowBox[{"(", 
        RowBox[{
         RowBox[{
          RowBox[{"-", "1"}], "*", 
          RowBox[{"(", 
           RowBox[{"0", "  ", "+", " ", "w2", "+", "  ", "wb"}], ")"}]}], "-",
          "1"}], ")"}]}], "\[Equal]", "0"}], ",", "\[IndentingNewLine]", 
     "         ", 
     RowBox[{"w1", " ", "\[Equal]", "  ", 
      RowBox[{"a1", " ", "+", " ", "a2"}]}], ",", "\[IndentingNewLine]", 
     "         ", 
     RowBox[{"w2", " ", "\[Equal]", "  ", 
      RowBox[{"a1", " ", "-", " ", "a4"}]}], ",", "\[IndentingNewLine]", 
     RowBox[{"a1", "\[GreaterEqual]", " ", "0"}], ",", 
     RowBox[{"a2", "\[GreaterEqual]", "0"}], ",", 
     RowBox[{"a3", "\[GreaterEqual]", " ", "0"}], ",", " ", 
     RowBox[{"a4", "\[GreaterEqual]", "0"}], ",", "\[IndentingNewLine]", 
     RowBox[{
      RowBox[{"a1", " ", "+", " ", "a2", " ", "+", "a3", "+", "a4"}], 
      "\[NotEqual]", " ", "0"}]}], "\[IndentingNewLine]", "}"}], ",", " ", 
   RowBox[{"{", 
    RowBox[{
    "w1", ",", "w2", ",", "a1", ",", "a2", ",", "a3", ",", "a4", ",", "wb"}], 
    "}"}]}], "\[IndentingNewLine]", "]"}]], "Input",
 CellChangeTimes->{{3.809474834952978*^9, 3.809475070818982*^9}, {
   3.809475104869767*^9, 3.809475135693948*^9}, {3.8094752630015717`*^9, 
   3.809475278239767*^9}, {3.809476181448061*^9, 3.8094761969675617`*^9}, {
   3.8094764029574823`*^9, 3.809476465940446*^9}, {3.8094766098231792`*^9, 
   3.8094766098894*^9}, {3.8094768205598907`*^9, 3.809476822023325*^9}, {
   3.8094825526172247`*^9, 3.809482564685861*^9}, 3.809482597800106*^9, {
   3.8111223626559134`*^9, 3.811122363239992*^9}, {3.811123879672145*^9, 
   3.8111238929909706`*^9}},
 CellLabel->"In[2]:=",ExpressionUUID->"1373a607-9769-4c45-bcb7-d45841e89e7c"],

Cell[BoxData[
 TemplateBox[{
  "Solve", "svars", 
   "\"Equations may not give solutions for all \\\"solve\\\" variables.\"", 2,
    2, 1, 17672614559785304766, "Local"},
  "MessageTemplate"]], "Message", "MSG",
 CellChangeTimes->{{3.809475023770563*^9, 3.809475050376463*^9}, 
   3.8094750923806753`*^9, 3.8094751363411093`*^9, 3.809475278893475*^9, 
   3.8094761974817266`*^9, {3.809476466685459*^9, 3.8094764850314693`*^9}, 
   3.8094768230659733`*^9, 3.8094825987079887`*^9, 3.811123897872947*^9},
 CellLabel->
  "During evaluation of \
In[2]:=",ExpressionUUID->"8502c5fb-c163-49da-8ba4-bfbaf67c9c22"],

Cell[BoxData[
 RowBox[{"{", 
  RowBox[{
   RowBox[{"{", 
    RowBox[{
     RowBox[{"w1", "\[Rule]", 
      TemplateBox[{"2", 
        RowBox[{"0", "<", "a4", "<", "2"}]},
       "ConditionalExpression"]}], ",", 
     RowBox[{"w2", "\[Rule]", 
      TemplateBox[{"0", 
        RowBox[{"0", "<", "a4", "<", "2"}]},
       "ConditionalExpression"]}], ",", 
     RowBox[{"a1", "\[Rule]", 
      TemplateBox[{"a4", 
        RowBox[{"0", "<", "a4", "<", "2"}]},
       "ConditionalExpression"]}], ",", 
     RowBox[{"a2", "\[Rule]", 
      TemplateBox[{
        RowBox[{"2", "-", "a4"}], 
        RowBox[{"0", "<", "a4", "<", "2"}]},
       "ConditionalExpression"]}], ",", 
     RowBox[{"a3", "\[Rule]", 
      TemplateBox[{
        RowBox[{"2", "-", "a4"}], 
        RowBox[{"0", "<", "a4", "<", "2"}]},
       "ConditionalExpression"]}], ",", 
     RowBox[{"wb", "\[Rule]", 
      TemplateBox[{
        RowBox[{"-", "1"}], 
        RowBox[{"0", "<", "a4", "<", "2"}]},
       "ConditionalExpression"]}]}], "}"}], ",", 
   RowBox[{"{", 
    RowBox[{
     RowBox[{"w1", "\[Rule]", "1"}], ",", 
     RowBox[{"w2", "\[Rule]", 
      RowBox[{"-", "1"}]}], ",", 
     RowBox[{"a1", "\[Rule]", "0"}], ",", 
     RowBox[{"a2", "\[Rule]", "1"}], ",", 
     RowBox[{"a3", "\[Rule]", "0"}], ",", 
     RowBox[{"a4", "\[Rule]", "1"}], ",", 
     RowBox[{"wb", "\[Rule]", "0"}]}], "}"}], ",", 
   RowBox[{"{", 
    RowBox[{
     RowBox[{"w1", "\[Rule]", "1"}], ",", 
     RowBox[{"w2", "\[Rule]", "1"}], ",", 
     RowBox[{"a1", "\[Rule]", "1"}], ",", 
     RowBox[{"a2", "\[Rule]", "0"}], ",", 
     RowBox[{"a3", "\[Rule]", "1"}], ",", 
     RowBox[{"a4", "\[Rule]", "0"}], ",", 
     RowBox[{"wb", "\[Rule]", 
      RowBox[{"-", "1"}]}]}], "}"}], ",", 
   RowBox[{"{", 
    RowBox[{
     RowBox[{"w1", "\[Rule]", "2"}], ",", 
     RowBox[{"w2", "\[Rule]", "0"}], ",", 
     RowBox[{"a1", "\[Rule]", "0"}], ",", 
     RowBox[{"a2", "\[Rule]", "2"}], ",", 
     RowBox[{"a3", "\[Rule]", "2"}], ",", 
     RowBox[{"a4", "\[Rule]", "0"}], ",", 
     RowBox[{"wb", "\[Rule]", 
      RowBox[{"-", "1"}]}]}], "}"}], ",", 
   RowBox[{"{", 
    RowBox[{
     RowBox[{"w1", "\[Rule]", "2"}], ",", 
     RowBox[{"w2", "\[Rule]", "0"}], ",", 
     RowBox[{"a1", "\[Rule]", "2"}], ",", 
     RowBox[{"a2", "\[Rule]", "0"}], ",", 
     RowBox[{"a3", "\[Rule]", "0"}], ",", 
     RowBox[{"a4", "\[Rule]", "2"}], ",", 
     RowBox[{"wb", "\[Rule]", 
      RowBox[{"-", "1"}]}]}], "}"}]}], "}"}]], "Output",
 CellChangeTimes->{{3.809475023779682*^9, 3.809475050380417*^9}, 
   3.80947509238743*^9, 3.809475136345537*^9, 3.809475278916581*^9, 
   3.809476197500022*^9, {3.809476466690816*^9, 3.809476485036913*^9}, 
   3.809476823072219*^9, 3.809482598714428*^9, 3.811123897923832*^9},
 CellLabel->"Out[2]=",ExpressionUUID->"99f12a5c-36d8-4560-8e56-3f757fe12148"]
}, Open  ]],

Cell[TextData[StyleBox["Example 3", "Section"]], "Text",
 CellChangeTimes->{{3.809536430703939*^9, 
  3.809536434198866*^9}},ExpressionUUID->"18eb49a7-0edb-4701-9f49-\
965976f4799a"],

Cell["\<\
Class + 1 : (1, 1) and (0, 1)
Class - 1 : (0, 0) and (1, 0).\
\>", "Text",
 CellChangeTimes->{{3.8095366123505*^9, 
  3.8095366659743834`*^9}},ExpressionUUID->"68561c3b-ddbb-43d3-b954-\
474a76d63435"],

Cell[CellGroupData[{

Cell[BoxData[{
 RowBox[{
  RowBox[{"plt1", "=", " ", 
   RowBox[{"ListPlot", "[", 
    RowBox[{
     RowBox[{"{", 
      RowBox[{
       RowBox[{"{", 
        RowBox[{"0", ",", "0"}], "}"}], ",", 
       RowBox[{"{", 
        RowBox[{"1", ",", "0"}], "}"}]}], "}"}], ",", " ", 
     RowBox[{"PlotStyle", "\[Rule]", 
      RowBox[{"{", 
       RowBox[{
        RowBox[{"AbsolutePointSize", "[", "20", "]"}], ",", " ", "Red"}], 
       "}"}]}], ",", " ", 
     RowBox[{"AspectRatio", "\[Rule]", "1"}], ",", " ", 
     RowBox[{"PlotRange", "\[Rule]", 
      RowBox[{"{", 
       RowBox[{
        RowBox[{"{", 
         RowBox[{
          RowBox[{"-", "0.1"}], ",", " ", "1.1"}], "}"}], ",", " ", 
        RowBox[{"{", 
         RowBox[{
          RowBox[{"-", "0.1"}], ",", " ", "1.1"}], "}"}]}], "}"}]}]}], 
    "]"}]}], ";"}], "\[IndentingNewLine]", 
 RowBox[{
  RowBox[{"plt2", "=", " ", 
   RowBox[{"ListPlot", "[", 
    RowBox[{
     RowBox[{"{", 
      RowBox[{
       RowBox[{"{", 
        RowBox[{"0", ",", "1"}], "}"}], ",", 
       RowBox[{"{", 
        RowBox[{"1", ",", "1"}], "}"}]}], "}"}], ",", " ", 
     RowBox[{"PlotStyle", "\[Rule]", 
      RowBox[{"{", 
       RowBox[{
        RowBox[{"AbsolutePointSize", "[", "20", "]"}], ",", " ", "Blue"}], 
       "}"}]}], ",", " ", 
     RowBox[{"AspectRatio", "\[Rule]", "1"}], ",", " ", 
     RowBox[{"PlotRange", "\[Rule]", "All"}]}], "]"}]}], 
  ";"}], "\[IndentingNewLine]", 
 RowBox[{
  RowBox[{"plt3", " ", "=", 
   RowBox[{"ListLinePlot", "[", 
    RowBox[{
     RowBox[{"{", 
      RowBox[{
       RowBox[{"{", 
        RowBox[{"0", ",", "0.5"}], "}"}], ",", 
       RowBox[{"{", 
        RowBox[{"1", ",", " ", "0.5"}], "}"}]}], "}"}], ",", " ", 
     RowBox[{"PlotRange", "\[Rule]", "All"}], ",", " ", 
     RowBox[{"PlotStyle", "\[Rule]", 
      RowBox[{"{", 
       RowBox[{
        RowBox[{"Thickness", "[", ".01", "]"}], ",", " ", "Black"}], 
       "}"}]}]}], "]"}]}], ";"}], "\[IndentingNewLine]", 
 RowBox[{"Show", "[", 
  RowBox[{"plt1", ",", " ", "plt2", ",", " ", "plt3"}], "]"}]}], "Input",
 CellChangeTimes->{{3.8095369025027103`*^9, 3.809536903306553*^9}, {
   3.809537043351777*^9, 3.809537060928832*^9}, {3.809537102176292*^9, 
   3.809537174966713*^9}, {3.809537222311054*^9, 3.8095372965615177`*^9}, {
   3.809537338669487*^9, 3.809537420583165*^9}, 3.809537603927072*^9, {
   3.809537672336062*^9, 3.8095377287711678`*^9}, {3.809537827438102*^9, 
   3.809537835365366*^9}},
 CellLabel->"In[80]:=",ExpressionUUID->"03979736-e039-4834-879d-163be819060e"],

Cell[BoxData[
 GraphicsBox[{{{}, {
     {RGBColor[1, 0, 0], AbsolutePointSize[20], AbsoluteThickness[1.6], 
      PointBox[{{0., 0.}, {1., 0.}}]}, {
      {RGBColor[1, 0, 0], AbsolutePointSize[20], AbsoluteThickness[
       1.6]}, {}}, {
      {RGBColor[1, 0, 0], AbsolutePointSize[20], AbsoluteThickness[
       1.6]}, {}}}, {{}, {}}}, {{}, {
     {RGBColor[0, 0, 1], AbsolutePointSize[20], AbsoluteThickness[1.6], 
      PointBox[{{0., 1.}, {1., 1.}}]}, {
      {RGBColor[0, 0, 1], AbsolutePointSize[20], AbsoluteThickness[
       1.6]}, {}}, {
      {RGBColor[0, 0, 1], AbsolutePointSize[20], AbsoluteThickness[
       1.6]}, {}}}, {{}, {}}}, {{}, {{{}, {}, 
      {GrayLevel[0], PointSize[
        NCache[
         Rational[7, 360], 0.019444444444444445`]], Thickness[0.01], 
       LineBox[{{0., 0.5}, {1., 0.5}}]}}, 
     {GrayLevel[0], PointSize[
       NCache[
        Rational[7, 360], 0.019444444444444445`]], Thickness[0.01]}, {
      {GrayLevel[0], PointSize[
        NCache[
         Rational[7, 360], 0.019444444444444445`]], Thickness[0.01]}, {}}, {
      {GrayLevel[0], PointSize[
        NCache[
         Rational[7, 360], 0.019444444444444445`]], Thickness[
       0.01]}, {}}}, {{}, {}}}},
  AspectRatio->1,
  Axes->{True, True},
  AxesLabel->{None, None},
  AxesOrigin->{0, 0},
  DisplayFunction->Identity,
  Frame->{{False, False}, {False, False}},
  FrameLabel->{{None, None}, {None, None}},
  FrameTicks->{{Automatic, Automatic}, {Automatic, Automatic}},
  GridLines->{None, None},
  GridLinesStyle->Directive[
    GrayLevel[0.5, 0.4]],
  ImageSize->{247., Automatic},
  Method->{
   "OptimizePlotMarkers" -> True, 
    "CoordinatesToolOptions" -> {"DisplayFunction" -> ({
        (Identity[#]& )[
         Part[#, 1]], 
        (Identity[#]& )[
         Part[#, 2]]}& ), "CopiedValueFunction" -> ({
        (Identity[#]& )[
         Part[#, 1]], 
        (Identity[#]& )[
         Part[#, 2]]}& )}},
  PlotRange->{{-0.1, 1.1}, {-0.1, 1.1}},
  PlotRangeClipping->True,
  PlotRangePadding->{{0, 0}, {0, 0}},
  Ticks->{Automatic, Automatic}]], "Output",
 CellChangeTimes->{
  3.809536904412709*^9, 3.8095370490058937`*^9, {3.8095371092402143`*^9, 
   3.809537123664385*^9}, 3.809537176394758*^9, {3.809537229945423*^9, 
   3.8095372672458563`*^9}, 3.8095372973919973`*^9, {3.80953735840058*^9, 
   3.809537389717016*^9}, 3.809537421292337*^9, 3.8095376058388033`*^9, {
   3.809537684678845*^9, 3.809537729764172*^9}},
 CellLabel->"Out[83]=",ExpressionUUID->"7f6e04a4-87dc-4246-ab12-c184883b3a8a"]
}, Open  ]],

Cell[CellGroupData[{

Cell[BoxData[
 RowBox[{"Solve", "[", 
  RowBox[{
   RowBox[{"{", 
    RowBox[{
     RowBox[{
      RowBox[{"a1", "-", "a2", "-", "a3", " ", "+", "a4"}], " ", "\[Equal]", 
      " ", "0"}], ",", "\[IndentingNewLine]", "         ", 
     RowBox[{
      RowBox[{"a1", " ", "*", 
       RowBox[{"(", 
        RowBox[{
         RowBox[{"1", "*", 
          RowBox[{"(", 
           RowBox[{"w1", "+", "w2", "+", "wb"}], ")"}]}], "-", "1"}], ")"}]}],
       "\[Equal]", "0"}], ",", "\[IndentingNewLine]", "         ", 
     RowBox[{
      RowBox[{"a2", "*", 
       RowBox[{"(", 
        RowBox[{
         RowBox[{
          RowBox[{"-", "1"}], "*", 
          RowBox[{"(", 
           RowBox[{"w1", "+", " ", "0", "+", "  ", "wb"}], ")"}]}], "-", 
         "1"}], ")"}]}], "\[Equal]", "0"}], ",", "\[IndentingNewLine]", 
     "         ", 
     RowBox[{
      RowBox[{"a3", "*", 
       RowBox[{"(", 
        RowBox[{
         RowBox[{
          RowBox[{"-", "1"}], "*", 
          RowBox[{"(", 
           RowBox[{"0", "  ", "+", " ", "0", "+", "  ", "wb"}], ")"}]}], "-", 
         "1"}], ")"}]}], "\[Equal]", "0"}], ",", "\[IndentingNewLine]", 
     "         ", 
     RowBox[{
      RowBox[{"a4", "*", 
       RowBox[{"(", 
        RowBox[{
         RowBox[{"1", "*", 
          RowBox[{"(", 
           RowBox[{"0", "  ", "+", " ", "w2", "+", "  ", "wb"}], ")"}]}], "-",
          "1"}], ")"}]}], "\[Equal]", "0"}], ",", "\[IndentingNewLine]", 
     "         ", 
     RowBox[{"w1", " ", "\[Equal]", "  ", 
      RowBox[{"a1", " ", "-", " ", "a2"}]}], ",", "\[IndentingNewLine]", 
     "         ", 
     RowBox[{"w2", " ", "\[Equal]", "  ", 
      RowBox[{"a1", " ", "+", " ", "a4"}]}], ",", "\[IndentingNewLine]", 
     RowBox[{"a1", "\[GreaterEqual]", " ", "0"}], ",", 
     RowBox[{"a2", "\[GreaterEqual]", "0"}], ",", 
     RowBox[{"a3", "\[GreaterEqual]", " ", "0"}], ",", " ", 
     RowBox[{"a4", "\[GreaterEqual]", "0"}], ",", "\[IndentingNewLine]", 
     RowBox[{
      RowBox[{"a1", " ", "+", " ", "a2", " ", "+", "a3", "+", "a4"}], 
      "\[NotEqual]", " ", "0"}]}], "\[IndentingNewLine]", "}"}], ",", " ", 
   RowBox[{"{", 
    RowBox[{
    "w1", ",", "w2", ",", "a1", ",", "a2", ",", "a3", ",", "a4", ",", "wb"}], 
    "}"}]}], "\[IndentingNewLine]", "]"}]], "Input",
 CellChangeTimes->{{3.809477853997056*^9, 3.809477896807169*^9}, 
   3.809536421910923*^9, {3.8111245224876904`*^9, 3.8111245228243237`*^9}},
 CellLabel->"In[3]:=",ExpressionUUID->"b8dc1e23-7470-4de2-a65d-6bc92c5617b7"],

Cell[BoxData[
 TemplateBox[{
  "Solve", "svars", 
   "\"Equations may not give solutions for all \\\"solve\\\" variables.\"", 2,
    3, 2, 17672614559785304766, "Local"},
  "MessageTemplate"]], "Message", "MSG",
 CellChangeTimes->{3.8094778982207403`*^9, 3.809535872419345*^9, 
  3.811124526855666*^9},
 CellLabel->
  "During evaluation of \
In[3]:=",ExpressionUUID->"a8092480-22d2-4357-8e8e-86c5c33d9cb0"],

Cell[BoxData[
 RowBox[{"{", 
  RowBox[{
   RowBox[{"{", 
    RowBox[{
     RowBox[{"w1", "\[Rule]", 
      TemplateBox[{
        FractionBox[
         RowBox[{
           RowBox[{
             RowBox[{"-", "2"}], " ", 
             RowBox[{"(", 
               RowBox[{"2", "-", "a4"}], ")"}]}], "+", 
           RowBox[{"2", " ", 
             RowBox[{"(", 
               RowBox[{"2", "-", 
                 FractionBox[
                  RowBox[{"4", "-", 
                    RowBox[{"2", " ", 
                    RowBox[{"(", 
                    RowBox[{"2", "-", "a4"}], ")"}]}], "-", 
                    RowBox[{"2", " ", "a4"}]}], 
                  RowBox[{"2", "-", "a4"}]], "-", "a4"}], ")"}]}], "-", 
           RowBox[{"2", " ", "a4"}], "+", 
           RowBox[{"2", " ", 
             RowBox[{"(", 
               RowBox[{
                 FractionBox[
                  RowBox[{"4", "-", 
                    RowBox[{"2", " ", 
                    RowBox[{"(", 
                    RowBox[{"2", "-", "a4"}], ")"}]}], "-", 
                    RowBox[{"2", " ", "a4"}]}], 
                  RowBox[{"2", "-", "a4"}]], "+", "a4"}], ")"}]}]}], 
         RowBox[{"2", "-", "a4"}]], 
        RowBox[{"0", "<", "a4", "<", "2"}]},
       "ConditionalExpression"]}], ",", 
     RowBox[{"w2", "\[Rule]", 
      TemplateBox[{"2", 
        RowBox[{"0", "<", "a4", "<", "2"}]},
       "ConditionalExpression"]}], ",", 
     RowBox[{"a1", "\[Rule]", 
      TemplateBox[{
        RowBox[{"2", "-", "a4"}], 
        RowBox[{"0", "<", "a4", "<", "2"}]},
       "ConditionalExpression"]}], ",", 
     RowBox[{"a2", "\[Rule]", 
      TemplateBox[{
        RowBox[{"2", "-", 
          FractionBox[
           RowBox[{"4", "-", 
             RowBox[{"2", " ", 
               RowBox[{"(", 
                 RowBox[{"2", "-", "a4"}], ")"}]}], "-", 
             RowBox[{"2", " ", "a4"}]}], 
           RowBox[{"2", "-", "a4"}]], "-", "a4"}], 
        RowBox[{"0", "<", "a4", "<", "2"}]},
       "ConditionalExpression"]}], ",", 
     RowBox[{"a3", "\[Rule]", 
      TemplateBox[{
        RowBox[{
          FractionBox[
           RowBox[{"4", "-", 
             RowBox[{"2", " ", 
               RowBox[{"(", 
                 RowBox[{"2", "-", "a4"}], ")"}]}], "-", 
             RowBox[{"2", " ", "a4"}]}], 
           RowBox[{"2", "-", "a4"}]], "+", "a4"}], 
        RowBox[{"0", "<", "a4", "<", "2"}]},
       "ConditionalExpression"]}], ",", 
     RowBox[{"wb", "\[Rule]", 
      TemplateBox[{
        RowBox[{"-", "1"}], 
        RowBox[{"0", "<", "a4", "<", "2"}]},
       "ConditionalExpression"]}]}], "}"}], ",", 
   RowBox[{"{", 
    RowBox[{
     RowBox[{"w1", "\[Rule]", 
      RowBox[{"-", "1"}]}], ",", 
     RowBox[{"w2", "\[Rule]", "1"}], ",", 
     RowBox[{"a1", "\[Rule]", "0"}], ",", 
     RowBox[{"a2", "\[Rule]", "1"}], ",", 
     RowBox[{"a3", "\[Rule]", "0"}], ",", 
     RowBox[{"a4", "\[Rule]", "1"}], ",", 
     RowBox[{"wb", "\[Rule]", "0"}]}], "}"}], ",", 
   RowBox[{"{", 
    RowBox[{
     RowBox[{"w1", "\[Rule]", "0"}], ",", 
     RowBox[{"w2", "\[Rule]", "2"}], ",", 
     RowBox[{"a1", "\[Rule]", "0"}], ",", 
     RowBox[{"a2", "\[Rule]", "0"}], ",", 
     RowBox[{"a3", "\[Rule]", "2"}], ",", 
     RowBox[{"a4", "\[Rule]", "2"}], ",", 
     RowBox[{"wb", "\[Rule]", 
      RowBox[{"-", "1"}]}]}], "}"}], ",", 
   RowBox[{"{", 
    RowBox[{
     RowBox[{"w1", "\[Rule]", "0"}], ",", 
     RowBox[{"w2", "\[Rule]", "2"}], ",", 
     RowBox[{"a1", "\[Rule]", "2"}], ",", 
     RowBox[{"a2", "\[Rule]", "2"}], ",", 
     RowBox[{"a3", "\[Rule]", "0"}], ",", 
     RowBox[{"a4", "\[Rule]", "0"}], ",", 
     RowBox[{"wb", "\[Rule]", 
      RowBox[{"-", "1"}]}]}], "}"}], ",", 
   RowBox[{"{", 
    RowBox[{
     RowBox[{"w1", "\[Rule]", "1"}], ",", 
     RowBox[{"w2", "\[Rule]", "1"}], ",", 
     RowBox[{"a1", "\[Rule]", "1"}], ",", 
     RowBox[{"a2", "\[Rule]", "0"}], ",", 
     RowBox[{"a3", "\[Rule]", "1"}], ",", 
     RowBox[{"a4", "\[Rule]", "0"}], ",", 
     RowBox[{"wb", "\[Rule]", 
      RowBox[{"-", "1"}]}]}], "}"}]}], "}"}]], "Output",
 CellChangeTimes->{3.8094778982293243`*^9, 3.8095358724248*^9, 
  3.81112452687262*^9},
 CellLabel->"Out[3]=",ExpressionUUID->"e161dc46-5190-4908-9514-cba2dfe850d2"]
}, Open  ]]
},
WindowSize->{958, 988},
WindowMargins->{{Automatic, -7}, {Automatic, 0}},
PrintingOptions->{"PrintCellBrackets"->True,
"PrintMultipleHorizontalPages"->False,
"PrintRegistrationMarks"->False,
"PrintingMargins"->14.4},
FrontEndVersion->"12.1 for Microsoft Windows (64-bit) (June 19, 2020)",
StyleDefinitions->"Default.nb",
ExpressionUUID->"9bd26cb1-dcd6-4d73-a0f9-ba0c4d747bb0"
]
(* End of Notebook Content *)

(* Internal cache information *)
(*CellTagsOutline
CellTagsIndex->{}
*)
(*CellTagsIndex
CellTagsIndex->{}
*)
(*NotebookFileOutline
Notebook[{
Cell[558, 20, 646, 11, 241, "Text",ExpressionUUID->"adb71a89-d562-47df-8324-6a36495c6a5b"],
Cell[1207, 33, 329, 5, 51, "Text",ExpressionUUID->"d4281001-2bb3-46e0-989d-06a0ef7d711b"],
Cell[CellGroupData[{
Cell[1561, 42, 597, 14, 28, "Input",ExpressionUUID->"d7fd43c0-1e1a-43c6-a25a-82658c8ea76f"],
Cell[2161, 58, 302, 8, 32, "Output",ExpressionUUID->"cf5fa7c2-8c1d-442e-89dc-69691adf891f"]
}, Open  ]],
Cell[2478, 69, 272, 5, 51, "Text",ExpressionUUID->"ed97af3f-f5e1-4ac0-a1c1-69273c6a9ff6"],
Cell[2753, 76, 585, 11, 56, "Text",ExpressionUUID->"0b7d98c4-9102-4544-ae34-f089afb92879"],
Cell[CellGroupData[{
Cell[3363, 91, 2230, 61, 105, "Input",ExpressionUUID->"4a9548ae-df9a-437e-90f4-a3af5227764e"],
Cell[5596, 154, 2221, 56, 241, "Output",ExpressionUUID->"27ad8ad9-8b11-4387-8920-fee108e2ea32"]
}, Open  ]],
Cell[CellGroupData[{
Cell[7854, 215, 1375, 37, 48, "ItemNumbered",ExpressionUUID->"a8e278eb-4b39-4600-a068-a4cb8d19a28f"],
Cell[9232, 254, 2167, 56, 110, "ItemNumbered",ExpressionUUID->"6c2db023-8746-4aea-bc62-84b9e8189e8e"],
Cell[11402, 312, 1492, 36, 48, "ItemNumbered",ExpressionUUID->"50f522f3-48fa-44d1-a642-a420f034480f"]
}, Open  ]],
Cell[12909, 351, 1164, 19, 56, "Text",ExpressionUUID->"0eb6bd6d-04ce-4aa1-b89c-7cb4d277c287"],
Cell[CellGroupData[{
Cell[14098, 374, 1411, 33, 162, "Input",ExpressionUUID->"f8b97ad5-0070-42a2-b0ba-49f0338d964d"],
Cell[15512, 409, 477, 12, 32, "Output",ExpressionUUID->"c3281e8d-8089-4eac-ae97-f586c71e18ef"]
}, Open  ]],
Cell[16004, 424, 839, 17, 78, "Text",ExpressionUUID->"54e97f20-029c-4bd4-b07b-b28ee1a48dde"],
Cell[16846, 443, 235, 4, 51, "Text",ExpressionUUID->"ee48dd51-a74f-4984-a51e-dc0bd061d2a6"],
Cell[17084, 449, 255, 7, 56, "Text",ExpressionUUID->"e01352ec-9ae0-4d87-986a-cdb9f4123047"],
Cell[CellGroupData[{
Cell[17364, 460, 2369, 66, 105, "Input",ExpressionUUID->"7871d66f-be0f-4091-a4e1-b2aac063d8e9"],
Cell[19736, 528, 2266, 57, 254, "Output",ExpressionUUID->"1c977473-74dd-4c42-be8d-7408b809eb53"]
}, Open  ]],
Cell[CellGroupData[{
Cell[22039, 590, 2903, 69, 219, "Input",ExpressionUUID->"1373a607-9769-4c45-bcb7-d45841e89e7c"],
Cell[24945, 661, 605, 12, 21, "Message",ExpressionUUID->"8502c5fb-c163-49da-8ba4-bfbaf67c9c22"],
Cell[25553, 675, 2832, 76, 127, "Output",ExpressionUUID->"99f12a5c-36d8-4560-8e56-3f757fe12148"]
}, Open  ]],
Cell[28400, 754, 182, 3, 51, "Text",ExpressionUUID->"18eb49a7-0edb-4701-9f49-965976f4799a"],
Cell[28585, 759, 210, 6, 56, "Text",ExpressionUUID->"68561c3b-ddbb-43d3-b954-474a76d63435"],
Cell[CellGroupData[{
Cell[28820, 769, 2538, 69, 105, "Input",ExpressionUUID->"03979736-e039-4834-879d-163be819060e"],
Cell[31361, 840, 2517, 61, 264, "Output",ExpressionUUID->"7f6e04a4-87dc-4246-ab12-c184883b3a8a"]
}, Open  ]],
Cell[CellGroupData[{
Cell[33915, 906, 2501, 63, 219, "Input",ExpressionUUID->"b8dc1e23-7470-4de2-a65d-6bc92c5617b7"],
Cell[36419, 971, 406, 10, 21, "Message",ExpressionUUID->"a8092480-22d2-4357-8e8e-86c5c33d9cb0"],
Cell[36828, 983, 4249, 117, 222, "Output",ExpressionUUID->"e161dc46-5190-4908-9514-cba2dfe850d2"]
}, Open  ]]
}
]
*)


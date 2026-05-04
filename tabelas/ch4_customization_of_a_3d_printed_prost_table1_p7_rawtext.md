# Customization of a 3D Printed Prosthetic Finger Using Parametric Modeling — CH4 Table 1

> Table could not be parsed automatically. Raw page text:

```
TABLE 1. Assorted length difference in percentage of 50 measure-
ments(uniformlyscaledandmeasurementslength)
further illustrates the need to use parametrized models because
thereisnoconsistantrelationshipbetweenrelativefingersizes. FIGURE7. TheSTLfileoftheaveragemodelwasuniformlyscaled
tofitthewidthofthemeasurement
3.2. Comparison of uniformly scaled and parametric
scaledmodels
From the measurements, we assumed building a prosthetic
finger for the participants index finger using two different de-
signmethods: uniformscalingandparametricmodeling. Forthe
uniformscalingmethod,areferencemodelwascreatedusingan
averageofthelength(90.9mm)andwidth(16.9mm). Ascurrent
3D printed prosthetic hands use a single parameter [7] for scal-
ingthereferencemodel,wescaledtheprostheticfingerfromthe
widthmeasurementofthefinger.
Using width for scaling ensures that the residual finger fits
the ring part of the device. From this reference, the files were FIGURE 8. Comparison between uniformly scaled and parametric
exported into the STL file format, and scaled uniformly using modeledCADfilesusingtwomeasurements.Thegreenmodelsusedan
3D printing slicer software CURA to retrieve the length of the indexfingeroflength86.06mmandawidthof19.56mm,length/width
indexfingerlengthL(Fig. 7). Fortheparametricmodeling,two ratio; 6.47. Theyellowmodelusedanindexoffingeroflength82.11
parameterswereinputintotheAutodeskFusion360parameters mmandawidthof12.69mm,length/widthratio;4.40.
user interface (Fig. 5), as fingerLength and fingerWidth, then
exportedintoSTLfiles.
The extracted measurements of prosthetic finger length us-
ingparametricmodelinganduniformscalingwereusedtocom- and a uniformly scaled model. Two index fingers which had a
paretheROMwithanoriginalfingermovement. Lengthdiffer- small 3.95 mm length difference (86.06 mm to 82.11mm) and
encewiththemeasuredfingerlengthandthedesignwerecalcu- a large difference in their length / width ratio were modeled
lated,thenassortedinto5%rangetosettheROMdifferencesin and compared. The green model was for a finger with a small
percentage. length to width ratio (4.40). The outer finger represents a uni-
Fortheuniformlyscaledmodel,48%ofthedesignedfinger formly scaled model (the resulting finger was 105.82mm) and
length were within the range of -5% to 5% of the actual finger theinnerfingerusedtheparametricmodel(resultingfingerwas
length (Table 1). However, 24% of the designed finger length 86.06mm). Theyellowcoloredmodelrepresentsanindexfinger
were longer than 5% of the actual length and 28% of the pop- withahighlengthtowidthratio(6.47),theoutsidemodelrepre-
ulation were shorter than -5% of actual length the range varied sents a uniformly scaled model (resulting finger was 68.65mm)
from -14.99% up to 25% of the reference length. On the other and the inner finger used a parametric designed model (result-
hand,parametricmodeledfingers’lengthwerealwaysinthe-5% ing finger was 82.11mm). In each case, the parametric model
to5%rangeasthewidthandthelengthwereindependent,thus matchedoriginallengthofthefinger. Usingauniformlyscaled
beingabletochangethelengthtotheexpectedvalue. modelcouldmakea37.17mm(105.82mm-68.65mm)lengthdif-
Figure8showsacomparisonbetweentheparametricmodel ferenceratherthantheactualdifferenceof3.95mm.
6 Copyright (cid:13)c 2018byASME
```

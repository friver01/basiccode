var data= [{
  "name": "placeHolder",
  "section": "right"
}, {
  "name": "Overview",
  "section": "left"
}, {
  "name": "ByFunction",
  "section": "left"
}, {
  "name": "Time",
  "section": "left"
}, {
  "name": "allFit",
  "section": "left"
}, {
  "name": "allbMatches",
  "section": "left"
}, {
  "name": "allOffers",
  "section": "left"
}, {
  "name": "allInterests",
  "section": "left"
}, {
  "name": "allResponses",
  "section": "left"
}, {
  "name": "divChanged",
  "section": "right"
}];
var index = data.findIndex(obj => obj.name=="allInterests");


alert (index);
$('ol').append (index);

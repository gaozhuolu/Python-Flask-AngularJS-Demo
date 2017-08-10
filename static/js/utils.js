function convertDate(datevalue, format) {
  var tmpdatevalue = new Date(datevalue);
  var momentDate = moment(tmpdatevalue);
  return momentDate.format(format);
}

function CSVConvertor(arrData, fileName) {
    var CSV = '';

    //1st loop is to extract each row
    for (var i = 0; i < arrData.length; i++) {
        var row = "";

        for (var index in arrData[i]) {
          if (arrData[i][index] != null && arrData[i][index] != 'null')
            row += '"' + arrData[i][index] + '",';
          else
            row += '"' + '",';
        }

        row.slice(0, row.length - 1);
        CSV += row + '\r\n';
    }

  var blob = new Blob([CSV], {type: "text/csv;charset=utf-8"});
  saveAs(blob, fileName+'.csv');
}

function switchName(strname){
  if(strname == '' || strname == null)
    return {firstname: '', lastname: ''}

  var splitName = strname.split(" ");
  var surname = splitName[splitName.length-1]; //The last one
  var firstnames = ""; // <- forgot to initialize to an empty string
  for (var i=0; i < splitName.length-1; i++){
    firstnames += splitName[i] + " "
  }

  return {firstname: firstnames, lastname: surname}
}

function GetFilename(url)
{
  return url.substring(url.lastIndexOf('/') + 1)
  //if (url)
  //{
  //   var m = url.toString().match(/.*\/(.+?)\./);
  //   if (m && m.length > 1)
  //   {
  //      return m[1];
  //   }
  //}
  //return "";
}

function getMonday(d) {
    d = new Date(d);
    var day = d.getDay(),
        diff = d.getDate() - day + (day == 0 ? -6:1); // adjust when day is sunday
    return new Date(d.setDate(diff));
}

function getMonthFirstDay(d) {
    d = new Date(d);
    d.setDate(1);
    return d;
}

function findSubStringInArray(strtarget, arrstrings) {
    for(var k = 0; k < arrstrings.length; k++) {
        if (arrstrings[k].toLowerCase().indexOf(strtarget.toLowerCase()) >= 0 && (arrstrings[k].indexOf(' ') >= 0 || arrstrings[k].indexOf(',') >= 0))
            return true;
    }

    return false;
}
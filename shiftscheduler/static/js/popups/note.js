// jshint esversion: 6

function noteOpen(step, year, month, day) {
  $.ajax({
    type: 'POST',
    url: '/html/note',
    contentType: 'application/json',
    data: JSON.stringify({
      step: step,
      year: year,
      month: month + 1,
      day: day
    }),
    success: function (data) {
      var container = $('div.note-container');
      container.html(data.html);
      container.css("display", "flex");
    },
    error: function (jq) {
      console.warn(jq.responseText);
      alert(jq.responseText);
    }
  });
}


function noteClose() {
  $('div.note-container').css("display", "none");
}


function noteBtnSubmit(orgStep, year, month, day) {
  // get data from popup element per id
  var newStep = $('select#note-step-select').val();
  var note = $('textarea#note-textarea').val();
  console.log(`${newStep}, ${note}`);

  $.ajax({
    type: 'POST',
    url: '/cache',
    contentType: 'application/json',
    data: JSON.stringify({
      date: `${year}/${month + 1}/${day}`,
      data: {
        step: newStep,
        note: note
      }
    }),
    success: function () {
      refreshScreen(month, year);
    },
    error: function (jq) {
      console.warn(jq.responseText);
      alert(jq.responseText);
    }
  });

  $('div.note-container').css("display", "none");
}


function noteBtnClear (step, year, month, day) {
  $.ajax({
    type: 'POST',
    url: '/cache',
    contentType: 'application/json',
    data: JSON.stringify({
      date: `${year}/${month + 1}/${day}`,
      data: {
        step: step,
        note: ''
      }
    }),
    success: function () {
      refreshScreen(month, year);
    },
    error: function (jq) {
      console.warn(jq.responseText);
      alert(jq.responseText);
    }
  });

  $('div.note-container').css("display", "none");
}


function noteBtnClearAll (year, month, day) {
  $.ajax({
    type: 'DELETE',
    url: '/cache',
    contentType: 'application/json',
    data: JSON.stringify({
      date: `${year}/${month + 1}/${day}`,
    }),
    success: function () {
      refreshScreen(month, year);
    },
    error: function (jq) {
      console.warn(jq.responseText);
      alert(jq.responseText);
    }
  });

  $('div.note-container').css("display", "none");
}

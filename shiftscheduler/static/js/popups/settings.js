// jshint esversion: 6

function settingsOpen() {
  $.ajax({
    type: 'GET',
    url: '/html/settings',
    success: function (data) {
      var container = $('div.settings-container');
      container.html(data.html);
      container.css("display", "flex");
    },
    error: function (jq) {
      console.warn(jq.responseText);
      alert(jq.responseText);
    }
  });
}


function settingsClose() {
  $('div.settings-container').css("display", "none");
}


function settingsSave() {
  let setup = {};

  $(".settings-group-input").each(function () {
    setup[this.name] = this.value;
  });

  $.ajax({
    url: '/config',
    type: 'POST',
    data: JSON.stringify(setup),
    contentType: "application/json",
    success: function () {
      refreshScreen(CACHE.month, CACHE.year);
      settingsClose();
    },
    error: function (jq) {
      console.warn(jq.responseText);
      alert(jq.responseText);
    }
  });
}

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
  // TODO iter elements from class 'popup-settings-input'
}

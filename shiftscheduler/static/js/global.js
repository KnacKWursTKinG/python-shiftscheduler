// jshint esversion: 6

// <<- Globals
const DATE = new Date();

const MONTHS = [
  "January", "February", "March", "April", "May", "June",
  "July", "August", "September", "October", "November", "December"
];

const DAYS = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];

const CACHE = {
  year: DATE.getFullYear(),
  month: DATE.getMonth()
};
// ->>


// <<- refreshScreen: create the grid for 'month' in 'year'
function refreshScreen(month, year, callback) {
  /* Main function to update the whole screen */
  if (month > 11) {
    // next year
    year = (year) ? year + 1 : CACHE.year + 1;
    month = 0;
  } else if (month < 0) {
    // prev year
    year = (year) ? year - 1 : CACHE.year - 1;
    month = 11;
  } else {
    year = (typeof year == 'undefined') ? CACHE.year : year;
    month = (typeof month == 'undefined') ? CACHE.month : month;
  }

  $.ajax({
    type: 'POST',
    url: '/html/month',
    data: JSON.stringify({
      month: month + 1, // NOTE: python month from 1..12
      year: year
    }),
    contentType: "application/json",
    success: function (data) {
      if (callback) {
        callback();
      }
      /* set new grid to body */
      $('.grid-container-body').html(data.html);

      $('.bottom-panel-string').html(`${year} ${MONTHS[month]}`);

      $('div.grid-item-body').click(function () {
        data = JSON.parse(this.id);  // NOTE: [day, 'step']

        noteOpen(data[1], year, month, data[0]);
      });

      // update cache
      CACHE.month = month;
      CACHE.year = year;
    },
    error: function (jq) {
      console.warn(jq.responseText);

      if ($('div.settings-container').css("display") !== 'none') {
        alert(jq.responseText);
      } else {
        settingsOpen();
      }
    }
  });
}
// ->>

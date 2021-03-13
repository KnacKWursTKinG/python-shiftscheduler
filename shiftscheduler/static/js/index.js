// jshint esversion: 6

// <<- Main
// first time refresh screen to draw the grid
refreshScreen();

$('.grid-container-head').html(() => {
  var html = '';

  DAYS.forEach((day) => {
    html += `<div class="grid-item-head grid-item">${day}</div>`;
  });

  return html;
});

$('div#year-prev').click(() => {
  refreshScreen(CACHE.month - 1);
});


$('div#year-next').click(() => {
  refreshScreen(CACHE.month + 1);
});


$('a.bottom-panel-string').click(() => {
  // TODO on slide insted of click
  settingsOpen();
});
// ->>

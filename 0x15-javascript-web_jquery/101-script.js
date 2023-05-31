'use strict';
$(() => {
  $('DIV#add_item').click(() => {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('DIV#remove_item').click(() => {
    const lastEl = $('UL.my_list').children().last();
    if (lastEl) {
      lastEl.remove();
    }
  });
  $('DIV#clear_list').click(() => {
    $('UL.my_list').empty();
  });
});

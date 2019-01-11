
$(function() {

  // some click handlers
  $('.overlay').on('click', function() {
    $('.overlay').addClass('hidden')
  })

  $('#btn').on('click', function() {
    $('.overlay').removeClass('hidden')
  })

  // the contact form stuff
  var server_message = document.getElementById('server-message')
  var url = new URL(document.location)
  var qs = url.searchParams
  var error = +qs.get('e')
  var sent = +qs.get('s')
  if (error && !sent) {
    server_message.textContent = 'Oops! Something went wrong...'
    return
  }
  if (!error && sent) {
    server_message.textContent = 'Thanks! Message sent.'
    return
  }
})

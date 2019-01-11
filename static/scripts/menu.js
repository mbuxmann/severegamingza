
var $ = jQuery

$(function() {
  
  /* 
    the above code '$(function() {' is equivalent to the following:
    
    window.addEventListener('DOMContentLoaded', function(e) {
      // your code here
    }, true)

    over time, we will write the equivalent standard javascript
    version of what this jquery code is doing. it makes our programs
    a little bit longer, generally, but overall our site has less
    code cause it wont include jquery.
  */

  $("nav ul li a:not(:only-child)").click(function(e) {

    // we have to tell the browser to ignore this click event
    // because we are going to override the default behaviour
    e.stopPropagation();

    // If a link has a dropdown, add sub menu toggle.
    $(this).siblings(".nav-dropdown").toggle();
    
    // Close one dropdown when selecting another
    $(".nav-dropdown").not(
      $(this).siblings()
    ).hide();
  });

  // Clicking away from dropdown will remove the dropdown class
  $("html").click(function() {
    $(".nav-dropdown").hide();
  });
  
  // Toggle open and close nav styles on click
  $("#nav-toggle").click(function() {
    $("nav ul").slideToggle();
  });
  
  // Hamburger to X toggle
  $("#nav-toggle").on("click", function() {
    this.classList.toggle("active");
  });
});
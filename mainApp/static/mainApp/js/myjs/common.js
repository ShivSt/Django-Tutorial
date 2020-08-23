// For Navigation: Add Dropdown options
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.dropdown-trigger');

    var options = {
        coverTrigger: false,    // show dropdown below its label
    }
    var instances = M.Dropdown.init(elems, options);
  });
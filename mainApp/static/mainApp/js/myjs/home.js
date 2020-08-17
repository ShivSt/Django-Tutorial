/* Use materializecss js functions/initializations only if you want to add any
options other than default. As default intialization for all the materializecss
components have done in header template with <script>M.AutoInit();</script> */


// Homepage: Add floating button options
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.fixed-action-btn');
    var options = {
                    direction: 'top',      //default='top'
                    hoverEnabled: true,    //default=true
                    //toolbarEnabled: true    //default=false
                }
    var instances = M.FloatingActionButton.init(elems, options);
});

// HomePage: Tooltip options for buttons
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.tooltipped');
    const options = {
        position: 'left',
    }
    var instances = M.Tooltip.init(elems, options);
});


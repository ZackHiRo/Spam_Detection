document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('predictionForm');
    const submitBtn = document.getElementById('submitBtn');
    const spinner = submitBtn.querySelector('.spinner-border');

    form.addEventListener('submit', function(e) {
        // Show loading state
        submitBtn.disabled = true;
        spinner.classList.remove('d-none');
        
        // Form will submit normally, this just handles the UI feedback
        setTimeout(() => {
            submitBtn.disabled = false;
            spinner.classList.add('d-none');
        }, 2000);
    });

    // Initialize all Bootstrap tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
});

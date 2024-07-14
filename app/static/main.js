document.addEventListener('DOMContentLoaded', (event) => {
    document.querySelectorAll('.patient-button').forEach(button => {
        button.addEventListener('click', () => {
            const patientId = button.getAttribute('data-patient-id');
            const doctorId = 1;  // Assuming a fixed doctor ID for now

            fetch('/access', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ doctor_id: doctorId, patient_id: patientId }),
            })
            .then(response => response.json())
            .then(data => {
                if (data.suspicious) {
                    alert('Suspicious activity detected!');
                }
            });
        });
    });
});

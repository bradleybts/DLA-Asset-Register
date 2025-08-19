document.addEventListener('DOMContentLoaded', () => {
    const assetForm = document.getElementById('register-asset-form');
    if (assetForm) {
        assetForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(assetForm);
            const data = Object.fromEntries(formData.entries());

            if (!data.assigned_to) {
                delete data.assigned_to;
            }

            try {
                const response = await fetch('/api/assets/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(data),
                });

                if (response.ok) {
                    alert('Asset registered successfully!');
                    assetForm.reset();
                } else {
                    const errorData = await response.json();
                    alert(`Error registering asset: ${JSON.stringify(errorData)}`);
                }
            } catch (error) {
                console.error('Error:', error);
                alert('An error occurred while registering the asset.');
            }
        });
    }

    const userForm = document.getElementById('user-registration-form');
    if (userForm) {
        const accessLevelSelect = document.getElementById('access_level');

        const populateAccessLevels = async () => {
            try {
                const response = await fetch('/api/user-classes/');
                if (response.ok) {
                    const userClasses = await response.json();
                    accessLevelSelect.innerHTML = '';
                    userClasses.forEach(userClass => {
                        const option = document.createElement('option');
                        option.value = userClass.id;
                        option.textContent = userClass.name;
                        accessLevelSelect.appendChild(option);
                    });
                }
            } catch (error) {
                console.error('Error fetching access levels:', error);
            }
        };

        populateAccessLevels();

        userForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(userForm);
            const data = Object.fromEntries(formData.entries());

            try {
                const response = await fetch('/api/users/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(data),
                });

                if (response.ok) {
                    alert('User registered successfully!');
                    userForm.reset();
                } else {
                    const errorData = await response.json();
                    alert(`Error registering user: ${JSON.stringify(errorData)}`);
                }
            } catch (error) {
                console.error('Error:', error);
                alert('An error occurred while registering the user.');
            }
        });
    }
});

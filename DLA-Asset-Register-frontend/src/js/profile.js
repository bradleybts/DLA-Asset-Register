document.addEventListener('DOMContentLoaded', function() {
  const profilePictureInput = document.getElementById('profile-picture');
  const profilePicture = document.getElementById('profile-picture-nav');

  // Load profile picture from local storage
  const savedPicture = localStorage.getItem('profilePicture');
  if (savedPicture && profilePicture) {
    profilePicture.style.backgroundImage = `url(${savedPicture})`;
  }

  // Handle profile picture update
  if (profilePictureInput && profilePicture) {
    profilePictureInput.addEventListener('change', function(event) {
      const file = event.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
          const imageDataUrl = e.target.result;
          localStorage.setItem('profilePicture', imageDataUrl);
          profilePicture.style.backgroundImage = `url(${imageDataUrl})`;
        }
        reader.readAsDataURL(file);
      }
    });
  }
});

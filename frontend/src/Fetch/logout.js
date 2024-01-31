document.getElementById('logoutBtn').addEventListener('click', function() {

    localStorage.removeItem('token');
   console.log('User has clicked the logout button. Logging out...');
 window.location.href = '../src/login.html';
});
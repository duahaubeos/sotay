
function goToPage2() {
    document.getElementById('page1').classList.add('hidden');
    document.getElementById('page1').classList.remove('active');
    
    document.getElementById('page2').classList.add('active');
}

function goToPage1() {
    document.getElementById('page2').classList.remove('active');
    
    document.getElementById('page1').classList.add('active');
    document.getElementById('page1').classList.remove('hidden');
}

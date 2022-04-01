var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("navDoctor").style.top = "0";
  } else {
    document.getElementById("navDoctor").style.top = "-50px";
  }
  prevScrollpos = currentScrollPos;
}

function openMenu() {
    document.getElementById("phoneNav").classList.add("phoneNavOpen")
    // document.getElementById("navHamburger").style.display = "none"
}

function closeMenu() {
    document.getElementById("phoneNav").classList.remove("phoneNavOpen")
    // document.getElementById("navHamburger").style.display = "block"
}
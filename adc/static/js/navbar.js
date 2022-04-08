const navitems = [
  "aboutus",
  "services",
  "doctors",
  "testimonials",
  "contactus",
];

$(document).ready(function () {
  $(window).on("load scroll", function () {
    // code for changing header bg color
    $(".fa-bars").removeClass("fa-times");
    $(".nav").removeClass("nav-toggle");
    if ($(window).scrollTop() > 10) {
      $(".lHeader").addClass("header-active");
    } else {
      $(".lHeader").removeClass("header-active");
    }
    // end code for changing header bg color

    // start code for changing header active menu color
    navitems.map((item) => {
      const elementPos = parseInt($(`#${item}`).offset().top) - 120;
      const currentPos = parseInt($(window).scrollTop());
      if (item === "contactus") console.log({ elementPos, currentPos });

      if (elementPos <= currentPos) {
        $(`#nav-${item}`).addClass("activeNavItem");
        navitems.map((prevItem) => {
          if (prevItem !== item) {
            $(`#nav-${prevItem}`).removeClass("activeNavItem");
          }
        });
      } else {
        $(`#nav-${item}`).removeClass("activeNavItem");
      }
    });
    // end code for changing header active menu color
  });
});

$(".faq__item").on("click", function () {
  $(this).toggleClass("active"),
    $(this).children(".faq__answer").slideToggle(300),
    $(this).children(".faq__circle").classList.toggle("minus");
});

$(".version1 .slider__wrapper").slick({
  infinite: !0,
  slidesToShow: 2,
  slidesToScroll: 1,
  prevArrow: $(".slider__btn--prev"),
  nextArrow: $(".slider__btn--next"),
  responsive: [
    { breakpoint: 1200, settings: { arrows: !1, dots: !0, slidesToShow: 1 } },
  ],
});

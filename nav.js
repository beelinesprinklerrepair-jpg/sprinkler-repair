/* Beeline site nav — ONE script for every page. */
(function(){
  var PHONE=680;
  function el(id){return document.getElementById(id)}
  function nav(){return document.querySelector('.site-nav')}
  function isOpen(){var m=el('mobileMenu');return !!(m&&m.classList.contains('open'))}
  function setMenu(open){
    var m=el('mobileMenu'),h=el('hamburger'),f=el('mobileNavFab'),n=nav();
    if(!m)return;
    m.classList.toggle('open',open);
    if(h){h.classList.toggle('open',open);h.setAttribute('aria-expanded',open?'true':'false')}
    if(f)f.classList.toggle('open',open);
    document.body.style.overflow=open?'hidden':'';
    if(open&&n){n.classList.remove('is-hidden');if(f)f.classList.remove('is-visible')}
  }
  function closeDropdowns(except){
    document.querySelectorAll('.site-nav .nav-dropdown.open').forEach(function(d){if(d!==except)d.classList.remove('open')});
  }
  // Capture phase so old per-page scripts can't double-toggle anything.
  document.addEventListener('click',function(e){
    var t=e.target.closest?e.target.closest('#hamburger,#mobileNavFab,.mobile-section-label,.site-nav .nav-dropdown-toggle,.mobile-menu a'):null;
    if(!t){closeDropdowns();return}
    if(t.id==='hamburger'||t.id==='mobileNavFab'){
      e.preventDefault();e.stopImmediatePropagation();setMenu(!isOpen());return;
    }
    if(t.classList.contains('mobile-section-label')){
      e.preventDefault();e.stopImmediatePropagation();
      var sub=t.nextElementSibling,open=sub.style.display!=='block',s=t.querySelector('span');
      sub.style.display=open?'block':'none';if(s)s.style.transform=open?'rotate(180deg)':'';
      return;
    }
    if(t.classList.contains('nav-dropdown-toggle')){
      e.preventDefault();e.stopImmediatePropagation();
      var d=t.parentElement,was=d.classList.contains('open');closeDropdowns(d);d.classList.toggle('open',!was);
      return;
    }
    setMenu(false); // tapped a link in the mobile menu
  },true);
  document.addEventListener('keydown',function(e){if(e.key==='Escape'){closeDropdowns();setMenu(false)}});

  // Phones: hide the bar after scrolling down, show the floating menu button instead.
  var ticking=false;
  function onScroll(){
    ticking=false;
    var n=nav(),f=el('mobileNavFab');if(!n)return;
    var hide=window.innerWidth<=PHONE&&window.scrollY>80&&!isOpen();
    n.classList.toggle('is-hidden',hide);
    if(f)f.classList.toggle('is-visible',hide);
  }
  window.addEventListener('scroll',function(){if(!ticking){ticking=true;requestAnimationFrame(onScroll)}},{passive:true});
  window.addEventListener('resize',function(){if(window.innerWidth>1100&&isOpen())setMenu(false);onScroll()});

  // Highlight the current page in the menus.
  function markActive(){
    var here=(location.pathname.split('/').pop()||'index.html').replace(/\.html$/,'')||'index';
    document.querySelectorAll('.site-nav a[href], .mobile-menu a[href]').forEach(function(a){
      var h=(a.getAttribute('href')||'').split('#')[0].split('/').pop().replace(/\.html$/,'');
      if(h&&h===here){
        a.classList.add('active');
        var dd=a.closest('.nav-dropdown');
        if(dd){var tg=dd.querySelector('.nav-dropdown-toggle');if(tg)tg.classList.add('active')}
      }
    });
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',function(){markActive();onScroll()});
  else{markActive();onScroll()}
})();

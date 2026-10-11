'use strict';
(function(){
  const year=document.getElementById('year');
  if(year) year.textContent=String(new Date().getFullYear());

  // Mobile menu. Without JavaScript the links stay visible (see .js rules in site.css).
  const toggle=document.querySelector('.nav-toggle');
  const nav=document.getElementById('nav');
  function closeMenu(){
    if(!toggle||!nav) return;
    nav.classList.remove('open');
    toggle.setAttribute('aria-expanded','false');
  }
  if(toggle&&nav){
    toggle.addEventListener('click',()=>{
      const open=nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded',String(open));
    });
    nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',closeMenu));
    document.addEventListener('keydown',e=>{
      if(e.key==='Escape'&&nav.classList.contains('open')){closeMenu();toggle.focus();}
    });
  }

  // Preserve the mobile Viber links confirmed by the site owner (V10 logic, unchanged
  // deep-link formats). V3 has several Viber buttons per page, so the same rewrite is
  // applied to each of them instead of only the first one.
  const vibers=document.querySelectorAll('[data-contact="viber"]');
  if(vibers.length){
    const ua=navigator.userAgent||'';
    const ios=/iPad|iPhone|iPod/i.test(ua)||(navigator.platform==='MacIntel'&&navigator.maxTouchPoints>1);
    const android=/Android/i.test(ua);
    vibers.forEach(viber=>{
      if(ios) viber.href='viber://contact?number=%2B38267998199';
      else if(android) viber.href='viber://chat?number=38267998199';
    });
    document.querySelectorAll('.viber-copy-button').forEach(copy=>{
      const feedback=copy.parentElement&&copy.parentElement.querySelector('.viber-copy-feedback');
      copy.addEventListener('click',async()=>{
        const number='+38267998199';
        try{
          if(!navigator.clipboard?.writeText) throw new Error('Clipboard API unavailable');
          await navigator.clipboard.writeText(number);
          if(feedback) feedback.textContent=copy.dataset.copied||'Copied';
        }catch(e){
          window.prompt(copy.dataset.manual||'Copy this number:',number);
        }
      });
    });
  }

  // Consent-gated measurement. All dev, preview and Cloudflare Pages URLs are
  // explicitly excluded, preventing real Ad conversions during site testing.
  const consentKey='tumac_ads_consent';
  const adsId='AW-837134242';
  const whatsAppConversion='drLwCI3GgpYdEKLPlo8D'; // confirmed on the supplied previous site
  const productionHosts=['tumac-njemacki.me','www.tumac-njemacki.me'];
  const isProduction=productionHosts.includes(window.location.hostname.toLowerCase());
  const panel=document.querySelector('[data-privacy-consent]');
  let inMemoryConsent=null;
  let adsInitialized=false;

  function readConsent(){
    try{return localStorage.getItem(consentKey)}catch(e){return inMemoryConsent}
  }
  function saveConsent(choice){
    inMemoryConsent=choice;
    try{localStorage.setItem(consentKey,choice)}catch(e){/* local fallback only */}
  }
  function renderConsent(){
    if(panel) panel.hidden=readConsent()!==null;
    updateDock();
  }
  function initializeAds(){
    if(!isProduction||readConsent()!=='yes'||adsInitialized) return;
    adsInitialized=true;
    window.dataLayer=window.dataLayer||[];
    window.gtag=window.gtag||function(){window.dataLayer.push(arguments)};
    // No analytics measurement or personalized advertising is requested.
    window.gtag('consent','default',{
      ad_storage:'denied',ad_user_data:'denied',
      ad_personalization:'denied',analytics_storage:'denied',
      wait_for_update:500
    });
    window.gtag('consent','update',{
      ad_storage:'granted',ad_user_data:'granted',
      ad_personalization:'denied',analytics_storage:'denied'
    });
    window.gtag('js',new Date());
    window.gtag('config',adsId);
    const tag=document.createElement('script');
    tag.async=true;
    tag.src='https://www.googletagmanager.com/gtag/js?id='+encodeURIComponent(adsId);
    document.head.appendChild(tag);
  }

  // Sticky contact bar on phones: shown only after the first contact buttons have
  // scrolled away, hidden in the contact section and while the consent notice is open.
  const dock=document.querySelector('[data-dock]');
  const dockState={pastHero:false,atContact:false};
  function updateDock(){
    if(!dock) return;
    const consentOpen=panel&&!panel.hidden;
    const show=dockState.pastHero&&!dockState.atContact&&!consentOpen;
    dock.classList.toggle('show',show);
    dock.toggleAttribute('inert',!show);
    dock.setAttribute('aria-hidden',String(!show));
    document.body.classList.toggle('has-dock',show);
  }
  if(dock&&'IntersectionObserver' in window){
    const heroActions=document.querySelector('[data-dock-after]');
    const contact=document.getElementById('kontakt');
    if(heroActions) new IntersectionObserver(entries=>{
      entries.forEach(en=>{dockState.pastHero=!en.isIntersecting&&en.boundingClientRect.top<0});
      updateDock();
    }).observe(heroActions);
    if(contact) new IntersectionObserver(entries=>{
      entries.forEach(en=>{dockState.atContact=en.isIntersecting});
      updateDock();
    },{rootMargin:'0px 0px -35% 0px'}).observe(contact);
  }

  if(panel){
    const accept=panel.querySelector('[data-consent-accept]');
    const reject=panel.querySelector('[data-consent-reject]');
    if(accept) accept.addEventListener('click',()=>{saveConsent('yes');renderConsent();initializeAds()});
    if(reject) reject.addEventListener('click',()=>{saveConsent('no');renderConsent()});
  }

  document.querySelectorAll('[data-privacy-settings]').forEach(el=>{
    el.addEventListener('click',e=>{
      e.preventDefault();
      // Reload so an already loaded Google script cannot continue running
      // in the same document after consent is withdrawn.
      inMemoryConsent=null;
      try{localStorage.removeItem(consentKey)}catch(err){/* no persistent access */}
      if(adsInitialized) window.location.reload();
      else renderConsent();
    });
  });

  initializeAds();
  renderConsent();

  document.addEventListener('click',e=>{
    const a=e.target.closest('a[data-contact="whatsapp"]');
    if(!a||!isProduction||readConsent()!=='yes'||typeof window.gtag!=='function')return;
    // A contact click is NOT a verified WhatsApp message or business lead.
    window.gtag('event','conversion',{
      send_to:adsId+'/'+whatsAppConversion
    });
  });
})();

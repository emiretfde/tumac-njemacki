'use strict';
(function(){
  const year=document.getElementById('year');
  if(year) year.textContent=String(new Date().getFullYear());

  const toggle=document.querySelector('.mobile-toggle');
  const nav=document.getElementById('nav');
  if(toggle&&nav){
    toggle.addEventListener('click',()=>{
      const open=nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded',String(open));
      toggle.classList.toggle('is-open',open);
    });
    nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{
      nav.classList.remove('open');
      toggle.setAttribute('aria-expanded','false');
      toggle.classList.remove('is-open');
    }));
  }

  // Preserve the mobile Viber links confirmed by the site owner.
  const viber=document.querySelector('[data-contact="viber"]');
  if(viber){
    const ua=navigator.userAgent||'';
    const ios=/iPad|iPhone|iPod/i.test(ua)||(navigator.platform==='MacIntel'&&navigator.maxTouchPoints>1);
    const android=/Android/i.test(ua);
    if(ios) viber.href='viber://contact?number=%2B38267998199';
    else if(android) viber.href='viber://chat?number=38267998199';
    const copy=document.querySelector('.viber-copy-button');
    const feedback=document.querySelector('.viber-copy-feedback');
    if(copy) copy.addEventListener('click',async()=>{
      const number='+38267998199';
      try{
        if(!navigator.clipboard?.writeText) throw new Error('Clipboard API unavailable');
        await navigator.clipboard.writeText(number);
        if(feedback) feedback.textContent=copy.dataset.copied||'Copied';
      }catch(e){
        window.prompt(copy.dataset.manual||'Copy this number:',number);
      }
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

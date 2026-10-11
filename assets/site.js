'use strict';
(function(){
const year=document.getElementById('year');if(year)year.textContent=String(new Date().getFullYear());
const toggle=document.querySelector('.mobile-toggle');
const nav=document.getElementById('nav');
if(toggle&&nav){
 toggle.addEventListener('click',()=>{const open=nav.classList.toggle('open');toggle.setAttribute('aria-expanded',String(open));toggle.classList.toggle('is-open',open)});
 nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{nav.classList.remove('open');toggle.setAttribute('aria-expanded','false');toggle.classList.remove('is-open')}));
}
const viber=document.querySelector('[data-contact="viber"]');
if(!viber)return;
const ua=navigator.userAgent||'';
const ios=/iPad|iPhone|iPod/i.test(ua)||(navigator.platform==='MacIntel'&&navigator.maxTouchPoints>1);
const android=/Android/i.test(ua);
if(ios)viber.href='viber://contact?number=%2B38267998199';
else if(android)viber.href='viber://chat?number=38267998199';
const btn=document.querySelector('.viber-copy-button');
const feedback=document.querySelector('.viber-copy-feedback');
if(btn)btn.addEventListener('click',async()=>{
 const number='+38267998199';
 try{
  if(!navigator.clipboard?.writeText)throw new Error('No clipboard access');
  await navigator.clipboard.writeText(number);
  if(feedback)feedback.textContent=btn.dataset.copied||'Copied';
 }catch(e){window.prompt(btn.dataset.manual||'Copy this phone number:',number)}
});
})();
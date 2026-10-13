(function(){
  'use strict';
  const button=document.querySelector('.language');
  let language='en';
  try { if(localStorage.getItem('agent-series-language')==='zh') language='zh'; } catch(_) {}
  function setLanguage(value){
    const zh=value==='zh';document.documentElement.lang=zh?'zh-Hans':'en';
    if(button){button.textContent=zh?'English':'中文';button.setAttribute('aria-label',zh?'Switch to English':'切换至中文');}
  }
  setLanguage(language);
  if(button){
    button.hidden=false;
    button.addEventListener('click',function(){
      language=document.documentElement.lang==='en'?'zh':'en';setLanguage(language);
      try{localStorage.setItem('agent-series-language',language);}catch(_){}
    });
  }
  const dialog=document.querySelector('.image-dialog');
  if(!dialog || !dialog.showModal)return;
  let trigger;
  document.querySelectorAll('[data-figure]').forEach(link=>link.addEventListener('click',event=>{
    if(event.ctrlKey||event.metaKey||event.shiftKey||event.altKey)return;
    event.preventDefault();trigger=link;
    const original=link.querySelector('img');
    dialog.querySelector('img').src=original.src;dialog.querySelector('img').alt=original.alt;
    dialog.querySelector('.dialog-title').textContent=link.dataset.title || original.alt;
    dialog.querySelector('.figure-source a').href=link.dataset.source;
    dialog.showModal();
  }));
  dialog.querySelector('.close-dialog').addEventListener('click',()=>dialog.close());
  dialog.addEventListener('click',event=>{
    if(event.target===dialog){
      const b=dialog.getBoundingClientRect();
      if(event.clientX<b.left||event.clientX>b.right||event.clientY<b.top||event.clientY>b.bottom)dialog.close();
    }
  });
  dialog.addEventListener('close',()=>{if(trigger)trigger.focus();});
})();

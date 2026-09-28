/* Melrakki Systems: close the Applications menu on outside click, Escape or link choice. */
(function(){
  var d=document.querySelectorAll('.nav-drop details');
  if(!d.length) return;
  function closeAll(except){ d.forEach(function(x){ if(x!==except) x.removeAttribute('open'); }); }
  document.addEventListener('click',function(e){ var t=e.target.closest('.nav-drop details'); closeAll(t); if(e.target.closest('.nav-drop .drop a')) closeAll(null); });
  document.addEventListener('keydown',function(e){ if(e.key==='Escape'){ d.forEach(function(x){ if(x.open){ x.removeAttribute('open'); x.querySelector('summary').focus(); } }); } });
})();

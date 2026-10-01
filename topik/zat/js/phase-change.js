const slider=document.querySelector('#tempSlider');
if(slider){
 const out=document.querySelector('#tempValue'),state=document.querySelector('#tempState'),note=document.querySelector('#tempNote');
 function update(){const t=Number(slider.value);out.textContent=t+' °C';
 if(t<0){state.textContent='Padat';note.textContent='Model air murni dalam keadaan setimbang pada tekanan sekitar 1 atm.';}
 else if(t===0){state.textContent='Titik leleh';note.textContent='Es dan air cair dapat berada bersama. Suhu saja tidak menentukan berapa bagian yang sudah mencair; energi yang dipindahkan juga berperan.';}
 else if(t<100){state.textContent='Cair';note.textContent='Dalam model kesetimbangan pada 1 atm, fase cair stabil. Penguapan dari permukaan tetap dapat terjadi di bawah 100 °C.';}
 else if(t===100){state.textContent='Titik didih';note.textContent='Air cair dan uap dapat berada bersama pada sekitar 1 atm. Mencapai 100 °C tidak berarti seluruh air langsung menjadi gas.';}
 else{state.textContent='Gas';note.textContent='Model kesetimbangan air murni pada sekitar 1 atm. Penggeser ini tidak mensimulasikan laju pemanasan atau kalor laten.';}}
 slider.setAttribute('aria-label','Suhu air dalam model kesetimbangan');slider.addEventListener('input',update);update();
}

function creaFecha(fecha) {
  if (fecha === '') return null;
  let x = fecha.split('-');
  return new Date(x[0], x[1]-1, x[2]);
}

function main() {
  formulario = document.getElementById('nueva-entrada');
  let x = formulario.querySelector('#id-ped');
  let y =formulario.querySelector('#fecha-ped');

  formulario.querySelector('#botoncito').addEventListener('click', (e) => {
    e.preventDefault();
    if (x.value.length < 21 || x.value.length < 18) {
      alert('introduzca un identificador vvalido')
    }
    if (y.value === "") {
      let today = new Date();
      let dd = String(today.getDate()).padStart(2, '0');
      let mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
      let yyyy = today.getFullYear();
      today = mm + '/' + dd + '/' + yyyy;
      y = today
    }
    formulario.submit();
  });

  lala = document.getElementById('super-form');
  let z = lala.querySelector('#identificador');
  let g = lala.querySelector('#cantidad');
  let h = lala.querySelector('#inicial')
  lala.querySelector('#chidito').addEventListener((e) => {
    e.preventDefault();
  });
}

main()

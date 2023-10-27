function creaFecha(fecha) {
  if (fecha === '') return null;
  let x = fecha.split('-');
  return new Date(x[0], x[1]-1, x[2]);
}

function main() {
  menu = document.getElementById('menu');
  botones = menu.querySelector('.tabs');
  menu.querySelector('#entradas').classList.add('tab--active');
  menu.querySelector('#salidas').classList.add('tab--deactive');
  menu.querySelector('#fisico').classList.add('tab--deactive');
  botones.querySelector('#btn1').classList.add('btn-primary');

  botones.addEventListener('click', (e) => {
			e.preventDefault();
			if ([...e.target.classList].includes('btn')) {
				const nombreBtn = e.target.dataset.tab;

				if (menu.querySelector('.btn-primary')) {
					menu.querySelector('.btn-primary').classList.remove('btn-primary');
				}
        if (menu.querySelector('.tab--active')) {
          menu.querySelector('.tab--active').classList.add('tab--deactive');
					menu.querySelector('.tab--active').classList.remove('tab--active');
				}
				e.target.classList.add('btn-primary');
        menu.querySelector(`#${nombreBtn}`).classList.add('tab--active')
        menu.querySelector(`#${nombreBtn}`).classList.remove('tab--deactive')
			}
		});

    const form_entradas = document.forms['form-entradas'];
    form_entradas.addEventListener('submit', (e) => {
      e.preventDefault();
      let datos = {
        hayPedimiento: form_entradas['pedi'].checked,
        hayEntrada: form_entradas['ent'].checked,
        hayProducto: form_entradas['pdts'].checked,
        hayUsuario: form_entradas['usrs'].checked,
        pedFchIni: creaFecha(form_entradas['pedi-ini'].value),
        pedFchFin: creaFecha(form_entradas['pedi-fin'].value),
        entFchIni: creaFecha(form_entradas['ent-ini'].value),
        entFchFin: creaFecha(form_entradas['ent-fin'].value),
        productos: form_entradas['pdts-sel'].value,
        usuarios: form_entradas['usrs-sel'].value,
      }
      if (datos.hayPedimiento) {
        if ((datos.pedFchFin < datos.pedFchIni) || (datos.pedFchFin == null || datos.pedFchIni == null)) {
          alert('Error fechas pedimiento: introduzca fechas correctas');
          return;
        }
      }
      if (datos.hayEntrada) {
        if ((datos.entFchFin < datos.entFchIni) || (datos.entFchFin == null || datos.entFchIni == null)) {
          alert('Error fechas entrada: introduzca fechas correctas');
          return;
        }
      }
      if (datos.hayProducto) {
        if (datos.productos == "") {
          alert('Selecciona al menos un producto');
          return;
        }
      }
      if (datos.hayUsuario) {
        if (datos.usuarios == "") {
          alert('Selecciona al menos un usuario');
          return;
        }
      }
      form_entradas.submit();
    });
}

 main()

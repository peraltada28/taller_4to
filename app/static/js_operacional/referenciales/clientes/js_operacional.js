$(async()=> {
    // Feliz 2023
    // todo lo que se ejecutara aqui, se hara luego de que el html este completo 
    // Bienvenidos a axios y REST

    
    const modal_clientes_formulario = $('#modal_clientes_formulario')
    const btn_clientes_agregar = $('#btn_clientes_agregar')
    const btn_clientes_enviar = $('#btn_clientes_enviar')

    try {
    
        // asignando el evento al boton agregar
        btn_clientes_agregar.on('click', () => {
            alert("ASD")
          // activando el modal, mostrando
          modal_clientes_formulario.modal('show')
        })

    } catch (error) {
        console.error(error)
    }

})
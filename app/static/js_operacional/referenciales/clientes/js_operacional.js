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
            $('txt_cli_nom_ape').val('')
            $('txt_cli_ci').val('')
            $('txt_cli_tel').val('')
            $('txt_cli_dir').val('')

            // activando el modal, mostrando
            modal_clientes_formulario.modal('show')
        })


        btn_clientes_enviar.on('click', async() => {

            // recolectar los datos que el usuario ha ingresado
            const codigo = $('#txt_cli_cod').val()
            const nombres = $('#txt_cli_nom_ape').val()
            const ci_o_ruc = $('#txt_cli_ci').val()
            const telefono = $('#txt_cli_tel').val()
            const direccion = $('#txt_cli_dir').val()

            if(nombres && nombres.trim() && ci_o_ruc && ci_o_ruc.trim() && telefono && telefono.trim() && direccion && direccion.trim()) {
                //definir el array de clientes
                //estirando los datos al dar click en btn_clientes_enviar
                const rec_clientes = {
                    rec_nombres: nombres.toUpperCase(),
                    rec_ci_o_ruc: ci_o_ruc,
                    rec_telefono: telefono,
                    rec_direccion: direccion.toUpperCase()
                }

                try {

                    //enviar la solicitud al servidor
                    const { data } = await axios.post('/clientes/agregar_clientes_rut', rec_clientes)

                    if(data.estado && data.estado !== 'error') {
                        // cerrar el modal
                        modal_clientes_formulario.modal('hide')
                        // mensaje exitoso
                        Notiflix.Report.success('Correcto', 'Se ha guardado el registro', 'Salir')
                        return
                    }

                    if(data.estado && data.estado === 'error') {
                        // cerrar el modal
                        modal_clientes_formulario.modal('hide')
                        // mensaje exitoso
                        Notiflix.Report.warning('Cuidado', 'No se ha guardado el registro', 'Salir')
                        console.error(data.mensaje)
                        return
                    }

                    Notiflix.Report.warnign('Cuidado', 'No se ha guardado el registro', 'Salir')

                    console.log(respuesta)


                } catch (error) {
                    console.log(error)
                }
            }
                
        })
    

    } catch (error) {
        console.error(error)
    }

})
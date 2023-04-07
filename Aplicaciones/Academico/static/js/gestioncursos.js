(function (){

    const btnEliminacion = document.querySelectorAll(".btn-eliminacion");

    btnEliminacion.forEach(btn=>{
        btn.addEventListener('click', (e)=>{
            const confirmacion = confirm('¿Seguro que desea eliminar el curso?');
            if(!confirmacion){
                e.preventDefault();
            }
        })
    })

    $('.alert').alert()

})();
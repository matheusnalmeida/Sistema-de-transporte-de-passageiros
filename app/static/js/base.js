$(document).ready(function(){
    updateNavBar();
    validateSucessRegisterRedirect();
});

function updateNavBar() {
    var currentHref = window.location.href;    
    $("#base-topnav a").each(function (index,el) {
        if(el.href === currentHref)
        {
            $(el).attr('class', 'active')
            return;
        }
        $(el).removeAttr('class');
    });
}

function validateSucessRegisterRedirect()
{
    var sucessRegisterMessage = sessionStorage.getItem('sucessRegister')
    if(!!sucessRegisterMessage)
    {
        toastr.success(sucessRegisterMessage)
    }
    sessionStorage.removeItem('sucessRegister');
}
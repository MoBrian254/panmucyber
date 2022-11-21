function sendMail(){
    var params = {
        name: document.getElementById("name").value,
        phone: document.getElementById("phone").value,
        email: document.getElementById("email").value,
        message: document.getElementById("message").value,
    };

    const serviceId = "service_8h3m49l";
    const templateId = "template_zu0mpll";

    emailjs.send(serviceId, templateId, params).then((res) => {
        document.getElementById("name").value = "";
        document.getElementById("phone").value = "";
        document.getElementById("email").value = "";
        document.getElementById("message").value = "";

        console.log(res);
        alert("Mail was successfully sent!!!")
    }).catch(
        (err) => console.log(err)
    );
}



// 关于页面交互脚本

document.addEventListener('DOMContentLoaded', function() {
    // 进度条动画
    const progressBars = document.querySelectorAll('.progress-bar');
    
    progressBars.forEach(bar => {
        const percentage = bar.getAttribute('aria-valuenow');
        bar.style.width = '0%';
        
        setTimeout(() => {
            bar.style.transition = 'width 1s ease-in-out';
            bar.style.width = percentage + '%';
        }, 300);
    });
    
    // 滚动动画初始化
    initScrollAnimation();
    
    // 工具提示初始化
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    const tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    });
});

// 滚动动画函数
function initScrollAnimation() {
    const elements = document.querySelectorAll('.animate-on-scroll');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animated');
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1
    });
    
    elements.forEach(element => {
        observer.observe(element);
    });
    
    // 时间线项目的特殊动画
    const timelineItems = document.querySelectorAll('.timeline-item');
    const timelineObserver = new IntersectionObserver((entries) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                setTimeout(() => {
                    entry.target.classList.add('animated');
                }, index * 200); // 每个项目延迟200ms出现
                timelineObserver.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1
    });
    
    timelineItems.forEach(item => {
        timelineObserver.observe(item);
    });
}

// 联系表单验证
const contactForm = document.getElementById('contact-form');

if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // 简单验证
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const message = document.getElementById('message').value;
        let isValid = true;
        
        if (!name.trim()) {
            setError('name', '请输入您的姓名');
            isValid = false;
        } else {
            clearError('name');
        }
        
        if (!email.trim()) {
            setError('email', '请输入您的邮箱地址');
            isValid = false;
        } else if (!isValidEmail(email)) {
            setError('email', '请输入有效的邮箱地址');
            isValid = false;
        } else {
            clearError('email');
        }
        
        if (!message.trim()) {
            setError('message', '请输入您的消息');
            isValid = false;
        } else {
            clearError('message');
        }
        
        if (isValid) {
            // 这里可以添加AJAX提交逻辑
            // 暂时用alert模拟成功提交
            alert('感谢您的留言！我会尽快回复您。');
            contactForm.reset();
        }
    });
}

function setError(fieldId, message) {
    const field = document.getElementById(fieldId);
    const errorElement = field.nextElementSibling || document.createElement('div');
    
    errorElement.className = 'invalid-feedback';
    errorElement.innerText = message;
    
    if (!field.nextElementSibling) {
        field.parentNode.appendChild(errorElement);
    }
    
    field.classList.add('is-invalid');
}

function clearError(fieldId) {
    const field = document.getElementById(fieldId);
    field.classList.remove('is-invalid');
}

function isValidEmail(email) {
    const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
} 
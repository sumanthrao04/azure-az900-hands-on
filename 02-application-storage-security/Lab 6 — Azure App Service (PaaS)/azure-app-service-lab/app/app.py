from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="theme-color" content="#f3f2ec">
        <meta name="description" content="An AZ-900 hands-on lab deploying a Python Flask application to Azure App Service.">
        <title>Azure App Service | AZ-900 Lab 06</title>
        <style>
            :root {
                color-scheme: light;
                --paper: #f3f2ec;
                --ink: #192725;
                --muted: #65716d;
                --line: #d6d9d1;
                --blue: #1768d2;
                --lime: #d9ef72;
                --coral: #ed795d;
                --mono: "Consolas", "Courier New", monospace;
                --sans: "Trebuchet MS", "Segoe UI", sans-serif;
            }

            * { box-sizing: border-box; }
            html { scroll-behavior: smooth; }
            body {
                margin: 0;
                color: var(--ink);
                background-color: var(--paper);
                background-image: linear-gradient(rgba(25, 39, 37, .035) 1px, transparent 1px), linear-gradient(90deg, rgba(25, 39, 37, .035) 1px, transparent 1px);
                background-size: 32px 32px;
                font-family: var(--sans);
                -webkit-font-smoothing: antialiased;
            }

            .page { width: min(1080px, calc(100% - 64px)); margin: 0 auto; }
            .topline { display: flex; justify-content: space-between; align-items: center; min-height: 72px; border-bottom: 1px solid var(--line); font: 11px var(--mono); text-transform: uppercase; }
            .brand { display: flex; align-items: center; gap: 10px; }
            .brand-mark { width: 12px; height: 12px; background: var(--blue); transform: rotate(45deg); }
            .topline-note { color: var(--muted); }
            main { padding: 54px 0 68px; }
            .hero { position: relative; overflow: hidden; padding: 44px; background: var(--ink); color: #fff; }
            .hero::after { position: absolute; top: -50px; right: -35px; width: 210px; height: 210px; border: 1px solid rgba(217, 239, 114, .25); border-radius: 50%; box-shadow: 0 0 0 24px rgba(217, 239, 114, .05), 0 0 0 48px rgba(217, 239, 114, .035); content: ""; pointer-events: none; }
            .eyebrow, .section-label { margin: 0 0 14px; color: var(--blue); font: 11px var(--mono); text-transform: uppercase; }
            .hero .eyebrow { color: var(--lime); }
            h1 { max-width: 700px; margin: 0; font-family: Georgia, "Times New Roman", serif; font-size: 58px; font-weight: 400; line-height: 1.04; }
            h1 span { color: var(--lime); }
            .hero-copy { max-width: 590px; margin: 20px 0 0; color: #d0dad4; font-size: 16px; line-height: 1.75; }
            .live-status { display: inline-flex; align-items: center; gap: 9px; margin-top: 28px; padding: 9px 12px; border: 1px solid rgba(217, 239, 114, .4); color: var(--lime); font: 10px var(--mono); text-transform: uppercase; }
            .live-dot { width: 7px; height: 7px; border-radius: 50%; background: var(--lime); box-shadow: 0 0 0 4px rgba(217, 239, 114, .12); }
            .facts { display: grid; grid-template-columns: repeat(4, 1fr); margin-top: 18px; border: 1px solid var(--line); background: rgba(255, 255, 255, .5); }
            .fact { min-height: 100px; padding: 20px 22px; }
            .fact + .fact { border-left: 1px solid var(--line); }
            .fact-label { display: block; margin-bottom: 10px; color: var(--muted); font: 10px var(--mono); text-transform: uppercase; }
            .fact-value { font-size: 16px; font-weight: 700; }
            .section { padding: 48px 0; border-bottom: 1px solid var(--line); }
            .section-head { display: flex; justify-content: space-between; align-items: end; gap: 30px; margin-bottom: 24px; }
            .section-label { margin-bottom: 9px; }
            h2 { margin: 0; font-size: 28px; line-height: 1.2; }
            .section-note { max-width: 370px; margin: 0; color: var(--muted); font-size: 13px; line-height: 1.7; }
            .flow { display: grid; grid-template-columns: repeat(4, 1fr); border-top: 1px solid var(--line); border-left: 1px solid var(--line); }
            .flow-step { min-height: 160px; padding: 20px; border-right: 1px solid var(--line); border-bottom: 1px solid var(--line); background: rgba(255, 255, 255, .42); }
            .step-number { color: var(--coral); font: 11px var(--mono); }
            .flow-step h3 { margin: 20px 0 8px; font-size: 16px; }
            .flow-step p { margin: 0; color: var(--muted); font-size: 12px; line-height: 1.7; }
            .services { display: grid; grid-template-columns: repeat(3, 1fr); gap: 0 28px; }
            .service { display: grid; grid-template-columns: 34px 1fr; gap: 12px; padding: 18px 0; border-top: 1px solid var(--line); }
            .service-mark { display: grid; width: 28px; height: 28px; place-items: center; background: var(--lime); color: var(--ink); font: 10px var(--mono); }
            .service h3 { margin: 2px 0 6px; font-size: 14px; }
            .service p { margin: 0; color: var(--muted); font-size: 12px; line-height: 1.6; }
            footer { display: flex; justify-content: space-between; gap: 16px; padding: 20px 0 28px; color: var(--muted); font: 10px var(--mono); text-transform: uppercase; }

            @media (max-width: 720px) {
                .page { width: min(100% - 36px, 560px); }
                main { padding: 36px 0 48px; }
                .hero { padding: 32px 26px; }
                .hero::after { top: -105px; right: -115px; }
                h1 { font-size: 46px; }
                .facts { grid-template-columns: 1fr 1fr; }
                .fact:nth-child(3) { border-left: 0; border-top: 1px solid var(--line); }
                .fact:nth-child(4) { border-top: 1px solid var(--line); }
                .section { padding: 38px 0; }
                .section-head { align-items: start; flex-direction: column; gap: 10px; }
                .flow { grid-template-columns: 1fr 1fr; }
                .services { grid-template-columns: 1fr 1fr; gap: 0 18px; }
            }

            @media (max-width: 420px) {
                .page { width: calc(100% - 28px); }
                .topline { min-height: 62px; font-size: 9px; }
                .hero { padding: 28px 20px; }
                h1 { font-size: 38px; }
                .hero-copy { font-size: 14px; }
                .fact { min-height: 86px; padding: 16px 12px; }
                .fact-value { font-size: 14px; }
                .flow { grid-template-columns: 1fr; }
                .flow-step { min-height: 0; }
                .flow-step h3 { margin-top: 12px; }
                .services { grid-template-columns: 1fr; }
                footer { flex-direction: column; gap: 8px; }
            }

            @media (prefers-reduced-motion: no-preference) {
                main { animation: arrive .55s ease-out both; }
                @keyframes arrive { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }
            }
        </style>
    </head>
    <body>
        <div class="page">
            <header class="topline">
                <div class="brand"><span class="brand-mark" aria-hidden="true"></span><span>Cloud Field Notes</span></div>
                <span class="topline-note">AZ-900 / Lab 06</span>
            </header>

            <main>
                <section class="hero" aria-labelledby="page-title">
                    <p class="eyebrow">Managed platform / Python deployment</p>
                    <h1 id="page-title">Azure App Service,<br><span>up and running.</span></h1>
                    <p class="hero-copy">A Flask application deployed to Microsoft's managed web app platform. App Service handles the hosting layer so the project can focus on the application.</p>
                    <div class="live-status" role="status"><span class="live-dot" aria-hidden="true"></span>Application successfully deployed</div>
                </section>

                <section class="facts" aria-label="Deployment configuration">
                    <div class="fact"><span class="fact-label">Service model</span><span class="fact-value">PaaS</span></div>
                    <div class="fact"><span class="fact-label">Runtime</span><span class="fact-value">Python / Flask</span></div>
                    <div class="fact"><span class="fact-label">Hosting</span><span class="fact-value">Linux</span></div>
                    <div class="fact"><span class="fact-label">Transport</span><span class="fact-value">HTTPS</span></div>
                </section>

                <section class="section" aria-labelledby="flow-title">
                    <div class="section-head">
                        <div><p class="section-label">01 / How the app gets here</p><h2 id="flow-title">Code to cloud, in four steps.</h2></div>
                        <p class="section-note">App Service provides a managed environment to host web apps without managing the underlying virtual machines.</p>
                    </div>
                    <div class="flow">
                        <article class="flow-step"><span class="step-number">01</span><h3>Write the app</h3><p>Build the web experience with Python and Flask.</p></article>
                        <article class="flow-step"><span class="step-number">02</span><h3>Choose the plan</h3><p>Select the App Service Plan for region, compute, and scale.</p></article>
                        <article class="flow-step"><span class="step-number">03</span><h3>Deploy</h3><p>Publish the application to a Linux-hosted App Service.</p></article>
                        <article class="flow-step"><span class="step-number">04</span><h3>Serve requests</h3><p>Users reach the running application over HTTPS.</p></article>
                    </div>
                </section>

                <section class="section" aria-labelledby="services-title">
                    <div class="section-head">
                        <div><p class="section-label">02 / Azure building blocks</p><h2 id="services-title">Services used in this lab.</h2></div>
                        <p class="section-note">Each resource has a distinct role in organizing, hosting, and securely serving the application.</p>
                    </div>
                    <div class="services">
                        <article class="service"><span class="service-mark" aria-hidden="true">01</span><div><h3>Resource Group</h3><p>Organizes related Azure resources.</p></div></article>
                        <article class="service"><span class="service-mark" aria-hidden="true">02</span><div><h3>App Service Plan</h3><p>Defines the hosting compute and scaling options.</p></div></article>
                        <article class="service"><span class="service-mark" aria-hidden="true">03</span><div><h3>Azure App Service</h3><p>Runs and manages the web application.</p></div></article>
                        <article class="service"><span class="service-mark" aria-hidden="true">04</span><div><h3>Linux Hosting</h3><p>Provides the operating environment for the app.</p></div></article>
                        <article class="service"><span class="service-mark" aria-hidden="true">05</span><div><h3>Python + Flask</h3><p>Application runtime and web framework.</p></div></article>
                        <article class="service"><span class="service-mark" aria-hidden="true">06</span><div><h3>HTTPS</h3><p>Encrypts traffic between the app and its users.</p></div></article>
                    </div>
                </section>
            </main>

            <footer><span>Learning by building</span><span>Microsoft Azure / AZ-900 / Lab 06</span></footer>
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run()
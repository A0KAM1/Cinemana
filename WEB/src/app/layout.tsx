import React from 'react';
import { Metadata } from 'next';
import './globals.css';

export const metaData: Metadata = {
    title: "Cinemana",
}

export default function RootLayout({
    children,
}: {
    children: React.ReactNode
}) {
    return (
        <html lang="pt-br">
            <body>
                <header className="w-full h-10 bg-red">This will be my navigation</header>
                <div>
                    {children}
                </div>
            </body>
        </html>
    )
}
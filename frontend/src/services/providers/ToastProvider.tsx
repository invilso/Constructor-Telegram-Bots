import React, { ReactElement, ReactNode, useState } from 'react';

import ToastContainer from 'react-bootstrap/ToastContainer';

import MessageToast, { MessageToastProps } from 'components/MessageToast';

import ToastContext from 'services/contexts/ToastContext';

export interface ToastProviderProps {
	children: ReactNode;
}

function ToastProvider({ children }: ToastProviderProps): ReactElement<ToastProviderProps> {
	const [toasts, setToasts] = useState<ReactElement[]>([]);

	function removeToast(toast: ReactElement): void {
		setToasts(prevToasts => prevToasts.filter(_toast => _toast !== toast));
	}

	function createMessageToast(props: Omit<MessageToastProps, 'onExited'>): void {
		const toast = <MessageToast key={Date.now()} {...props} onExited={() => removeToast(toast)} />;

		setToasts(prevToasts => [...prevToasts, toast]);
	}

	return (
		<ToastContext.Provider value={{ createMessageToast }}>
			<ToastContainer className='vstack position-fixed bottom-0 end-0 gap-3 p-3'>
				{toasts}
			</ToastContainer>
			{children}
		</ToastContext.Provider>
	);
}

export default ToastProvider;
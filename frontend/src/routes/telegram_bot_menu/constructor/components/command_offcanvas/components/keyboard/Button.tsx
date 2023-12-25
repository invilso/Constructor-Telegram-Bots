import React, { ReactNode } from 'react';

import InputGroup from 'react-bootstrap/InputGroup';
import Form from 'react-bootstrap/Form';
import RBButton from 'react-bootstrap/Button';

import { Data, ButtonData } from './Main';

import { DraggableProvided } from 'react-beautiful-dnd';

export interface ButtonProps {
	data: Data;
	index: number;
	button: ButtonData;
	provided: DraggableProvided;
	onChange: (index: number, button: ButtonData) => void;
	onDelete: (index: number) => void;
}

function Button({ data, index, button, provided, onChange, onDelete }: ButtonProps): ReactNode {
	return (
		<InputGroup
			ref={provided.innerRef}
			{...provided.draggableProps}
			{...provided.dragHandleProps}
		>
			<RBButton
				as='div'
				size='sm'
				variant='light'
				className='border bi bi-arrows-move p-auto'
				style={{ width: '31px', cursor: 'move' }}
			/>
			<Form.Control
				value={button.text}
				size='sm'
				className='text-center'
				placeholder={gettext('Название кнопки')}
				onChange={e => onChange(index, { ...button, text: e.target.value })}
			/>
			{(data.type === 'inline' || data.type === 'payment') && (
				button.url !== undefined ? (
					<Form.Control
						value={button.url}
						size='sm'
						className='text-center'
						placeholder='URL-адрес'
						onChange={e => onChange(index, { ...button, url: e.target.value })}
					/>
				) : (
					<RBButton
						size='sm'
						variant='secondary'
						className='bi bi-link-45deg p-0'
						style={{ width: '31px', fontSize: '16px' }}
						onClick={() => onChange(index, { ...button, url: '' })}
					/>
				)
			)}
			<RBButton
				size='sm'
				variant='danger'
				className='bi bi-x-lg p-0'
				style={{ width: '31px', WebkitTextStroke: '1.25px' }}
				onClick={() => onDelete(index)}
			/>
		</InputGroup>
	);
}

export default Button;
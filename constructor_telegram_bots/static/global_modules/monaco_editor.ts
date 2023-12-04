import monaco from 'monaco-editor';

export function updateEditorLayout(
	monacoEditor: monaco.editor.IStandaloneCodeEditor,
	shouldResetWidth: boolean = false,
): void {
	monacoEditor.layout({
		width: shouldResetWidth ? 0 : monacoEditor.getContainerDomNode().getBoundingClientRect().width,
		height: (monacoEditor.getModel() as monaco.editor.ITextModel).getLineCount() * 19,
	});
}

export const defaultEditorOptions: monaco.editor.IStandaloneEditorConstructionOptions = {
	minimap: {enabled: false},
	renderLineHighlight: 'none',
	lineNumbersMinChars: 3,
	overviewRulerLanes: 0,
	scrollBeyondLastLine: false,
	scrollbar: {vertical: 'hidden'},
	inlayHints: {enabled: 'off'},
}